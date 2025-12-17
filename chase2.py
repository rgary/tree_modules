# Copyright 2025 R. Gary Cutbill
# All rights reserved

'''Example tree decorator.
Decorators should be implemented as python generators that
returns a pixel array with 8 bit  RGB bytes packed into a
np_int32.

The passed in value of 'pixels' is a shared memory buffer
containing a numpy array.  It's better to modify this in
place so it doesn't have to be copied, but if you return a 
copy, the right thing will happen in the function that called you.

Tree speed is used to select the speed of rotation and direction
of turning for the tree.  0-stopped, 1-low, 2-medium, 3-fast. Negative
numbers turn in the opposite direction. Tree angle is an input value
providing a estimate of the angle of rotation in degrees from an
arbitrary starting point.

When updated, Form data will be kept updated with values from a CGI
form available on the tree web-server.

Use sleep() in the generator to control how long each frame is displayed. 
'''

import pdb
from time import sleep
from coords import *
from common_utils import test_loop

colors=[0xff0000,0x00ff00,0x0000ff,0xff400,0xff9000]

# Alternate red and green every second
def generator(pixels,tree_speed,tree_angle,form_data):
    pause_time=.25
    count=0
    numcolors=len(colors)
    while True:
        for i in range(numcolors):
            index=(count+i)%numcolors
            size=(num_pixels-index)//numcolors
            pixels[index:num_pixels:numcolors]=colors[i]*numcolors
            #slicefill(index,num_pixels,numcolors,colors[i])
        sleep(pause_time)
        yield (pixels,tree_speed.value)
        count += 1
    
if __name__=='__main__':
   test_loop(generator) 
