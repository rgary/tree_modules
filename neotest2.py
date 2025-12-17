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

# Adapted from https://docs.circuitpython.org/projects/neopixel/en/latest/examples.html
# Original copyright:
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import pdb
from time import sleep
from coords import *
from common_utils import test_loop
 
# Pattern helper function 
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return r<<16 | g<<8 | b
 
colors=[ 0xff0000, 0x00ff00, 0x0000ff ]

# A simple demo generator that sets all pixels to each color in turn followed by 
# a rainbow arrangment; for five rounds
#
# Pixels is a shared-memory numpy array of np_int32
# coords is an ordered list of lists of floats contains XYZ coordinates 
# for each pixel
# num_pixels is the length of the coords lists.
#
# Fill the pixels array with RGB values as desired and 
# yield. 
def generator(pixels,tree_speed,tree_angle,form_data):
    pause_time=1.0
    while True:
        for speed in [ 1, 3, 5, 2, 1, 0, -1, -2, -3, -2, -1, 0 ]:
            tree_speed.value=speed
            # One pass each of red, green, blue
            for j in colors:
                pixels[:]=[j]*num_pixels # fill pixels with one color
                yield (pixels,tree_speed.value)
                sleep(pause_time)
   
            # Then a rainbow pass
            for j in range(255):
                for i in range(num_pixels):
                    pixel_index = (i * 256 // num_pixels) + j
                    pixels[i] = wheel(pixel_index & 255)
                yield (pixels,tree_speed.value)
                sleep(pause_time/250)
     
    
if __name__=='__main__':
   #pdb.set_trace() 
   test_loop(generator) 
