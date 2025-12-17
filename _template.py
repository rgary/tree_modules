import pdb
from time import sleep
from coords import *
from common_utils import test_loop
 
'''This is a template generator that fills the tree with one color.'''
def generator(pixels,tree_speed,tree_angle,form_data):
    # Put any initialization code here, these would
    # be things that only happen once during the lifetime
    # of your generator
    pause_time=1.0

    # The work goes here.  Generally this is an infinate
    # loop that will yield at the end of each pass.
    while True:
        pixels[:]=[0xff0000]*num_pixels # fill pixels with one color
        yield (pixels,tree_speed.value)
        sleep(pause_time) 
    
'''If invoke your generator as a program, rather than importing it as
a module, common_utils.test_module will invoke it in a loop and print
each pass to stdout.  You might want to use pdb to debug your generator'''
if __name__=='__main__':
   # pdb.set_trace()    # optional if you want to step into your code
   test_loop(generator) 
     
