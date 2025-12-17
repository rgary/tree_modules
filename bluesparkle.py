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

# Put an HTML form here. The text in 'form' will be put on a web page
# inside of an HTML form tag. The result of the form will be updated in
# the form_data variable as a python dict
form='''
<input type="submit" name="red" value="0xff0000"/>
<input type="submit" name="green" value="0x00ff00"/>
<input type="submit" name="blue" value="0x0000ff"/>
'''

def sparkle(numleds,basecolor=0x0000E9,whitelen=18,bluelen=8):
    while True:
        for i in range(1,whitelen):
            yield 0xffffff
        for i in range(1,bluelen):
            yield 0x0000E9
    
def generator(pixels,tree_speed,tree_angle,form_data):
    delay=0.1
    prevcolor=0
    color=0x0000E9
    while True:
        if form_data is not None:
           pass   # form processing goes here
        if color!=prevcolor:
            gen=sparkle(num_pixels,color)
            prevcolor=color
        for i in range(num_pixels):
            c=next(gen)
            pixels[i]=c
        sleep(delay)
        yield (pixels,tree_speed.value)

if __name__=='__main__':
   test_loop(generator) 
     
