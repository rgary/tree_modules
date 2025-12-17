# Copyright 2025 R. Gary Cutbill
# All rights reserved

'''Simple Example of tree decorator.
Decorators should be implemented as python generators that
returns a pixel array with 8 bit  RGB bytes packed into a
np_int32. (numpy int32)

Note: The passed in value of 'pixels' is a shared memory buffer
containing a numpy array.  It's better to modify this in
place so it doesn't have to be copied, but if you return a 
copy, the right thing will happen in the function that called you.

There are two variable related to tree movement.  Both are synchronised
shared memory objects.  To update them or read them, use the '.value' 
field.  'tree_speed.value' is an small (likely single digit) value that you 
can set to request that the tree bases rotates.  A speed of 0 says
stop. A positive integer turns the tree clockwise and a negative integer
turns it counter clockwise. If you exceed the limits of the tree, this will
be set to the most extreme positive or negative value.

"tree_angle.value" is set by the control software to provide an approximate angle of 
rotation since the last time the tree was started. (There is not absolute 
reference.)  You can change this, but your changes will be ignored and overwritten.

Formdata is currently unused, but may provide access to web input in the future.

When your generator yields, it returns an entire frame of pixels to update on the tree.
Use sleep() in the generator to control how long each frame is displayed. 
'''

import pdb
from time import sleep
from coords import *
from common_utils import test_loop
 
colors=[ 0xff0000, 0x00ff00 ] # alternating red and green

# This is a simple demo generator that sets all pixels to 
# each color in an array in turn with one second pauses betwee
# color changes.
#
def generator(pixels,tree_speed,tree_angle,form_data):
    pause_time=1.0
    while True:
        # One pass each of red, green, blue
        for j in colors:
            pixels[:]=[j]*num_pixels # fill pixels with one color
            yield (pixels,tree_speed.value)
            sleep(pause_time)
    
if __name__=='__main__':
   test_loop(generator) 
     
