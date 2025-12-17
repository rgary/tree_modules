import sys
import numpy as np
from coords import num_pixels
from multiprocessing import shared_memory,Value,Semaphore

shm=None

'''Clean up the shared memory so it doesn't persist past the run'''
def shared_cleanup():
    if shm is not None:
        shm.unlink()

# A simple conditional function that wraps  print() for debugging.
def dprint(debug,prefix,*args,**kwargs):
   if debug:
      print(prefix,*args,**kwargs)

'''Return an shared memory (numpy) array for pixels'''
def pixels_init():
    # Create a shared memory block to hold to pixel light values as int32 (ie four hex bytes for RGB)
    # Shared memory clears the buffer, so all values are initialized to 0x0
    shm=shared_memory.SharedMemory(create=True, size=num_pixels*np.array(1,dtype=np.int32).nbytes)
    pixels = np.ndarray((num_pixels,),dtype=np.int32,buffer=shm.buf)
    return pixels

'''Create all of the shared memory objects needed for the tree except pixels'''
def shared_init():
    #Other Shared variables
    tree_speed=Value('i',0,lock=False)  # Requested +/- RPM of tree movement (can be limited by motor fuctions)
    tree_angle=Value('f',0)  # The current angle in degrees

    # The designer and decorator use strict alternation for updates. The semaphores are used to
    # implement a 'ping-pong' algorithm
    designer_sem=Semaphore(1)
    decorator_sem=Semaphore(0)
    
    # All processes need these arguments in this order. (Spoiler, designer also gets one extra 
    # ahead of the others.)
    shargs= (tree_speed,tree_angle,designer_sem,decorator_sem)

    return shargs

'''Set up shared memory, invoked shared memory and print the results of each generator pass.'''
def test_loop(generator):
    shm=shared_memory.SharedMemory(create=True, size=num_pixels*np.array(1,dtype=np.int32).nbytes)
    pixels = np.ndarray((num_pixels,),dtype=np.int32,buffer=shm.buf)

    shared_args=shared_init()  # Build the shared arguments 

    tree_speed=shared_args[0]
    tree_angle=shared_args[1]
    form_data=None
    fake_angle=0

    gen=generator(pixels,tree_speed,tree_angle,form_data)
    for (pixels,speed) in gen:
        print(f'pixels={pixels}\n...speed={speed} tree_speed.value={tree_speed.value} tree_angle.value={tree_angle.value}')
        # Fake some rotation numbers in case the generator uses them.
        if speed>0:
           fake_angle+=10*speed
           fake_angle%=360
           tree_angle.value=fake_angle
        if speed>3:
           tree_speed.value=3
        if speed<-3:
           tree_speed.value=3
        if speed>1000:
           tree_speed.value=0
