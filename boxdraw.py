import pdb
from time import sleep
from scipy.interpolate import RegularGridInterpolator as RGI
import numpy as np
from coords import *
from common_utils import test_loop


# Create a simple box with a red boarder and a white center
#
#              RRRRR
#              R   R
#              R W R
#              R   R
#              RRRRR
#
#
 
def generator(pixels,tree_speed,tree_angle,form_data):
    pause_time=60.0
    r=0xff0000
    w=0xffffff
    b=0x000000
    
    # gridline values along x and y
    x=np.linspace(-18,18,7)
    y=np.linspace(30,66,7)

    # Red box with a white center
    # Hand crafted image, later load it with opencv (which uses numpy too)
    data=np.array([[b,b,b,b,b,b,b],
               [b,r,r,r,r,r,b],
               [b,r,0,0,0,r,b],
               [b,r,0,w,0,r,b],
               [b,r,0,0,0,r,b],
               [b,r,r,r,r,r,b],
               [b,b,b,b,b,b,b]])

    # nearest so image pixel values are modified, everything else gets blue
    interp=RGI((x,y),data,method='nearest',fill_value=0x0000ff,bounds_error=False)

    while True:
        for i in range(num_pixels):
            pixels[i]=interp((coords_xyz[i][0],coords_xyz[i][2]))
        yield (pixels,tree_speed.value)
        sleep(pause_time)
    

if __name__=='__main__':
   test_loop(generator) 
     
