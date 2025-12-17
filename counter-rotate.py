import pdb
from time import sleep
from coords import *
from common_utils import test_loop

colors=[0xff0000, 0x00ff00, 0x0000ff ]
 
def generator(pixels,tree_speed,tree_angle,form_data):
    pause_time=1.0
    tree_speed.value=2
    prev_theta=400
    intstep=360//len(colors)
    while True:
        theta=tree_angle.value
        if theta!=prev_theta:
            for p in range(num_pixels):
                m=int(((coords_rtz[p][1]-theta)%360)//intstep)
                pixels[p]= colors[m]
            prev_theta=theta
            yield (pixels,tree_speed.value)
        else:
           sleep(.005)
    
if __name__=='__main__':
   test_loop(generator) 
     
