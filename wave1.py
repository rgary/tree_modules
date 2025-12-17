import pdb
from time import sleep
from coords import *
from common_utils import test_loop
import math

def wave1(pixels,num_pixels,colors=[0xff0000,0x00ff00,0x0000ff],delay=.05,steps=255):
    numcolors=len(colors)
    while True:
        for step in range(steps):
            alpha=1.0*step/steps
            for index in range(numcolors):
                offset=1.0*index/numcolors
                frac=coshift(alpha+offset)
                setfixedposition(pixels,num_pixels,index,numcolors,scalecolor(colors[index],frac))
            sleep(delay)
            yield

def scalecolor(color,frac):
    red=scalebyte((color&0xff0000)>>16,frac)
    green=scalebyte((color&0xff00)>>8,frac)
    blue=scalebyte((color&0xff),frac)
    return(red<<16|green<<8|blue)

def scalebyte(value,frac):
    return int(value*frac)

def setfixedposition(pixels,numpixels,index,numcolors,color):
    pixels[index:numpixels:numcolors]=[color]*len(pixels[index:numpixels:numcolors])

def coshift(alpha):
    return 0.5+0.5*math.cos(alpha*math.tau)

def generator(pixels,tree_speed,tree_angle,form_data):
    iter=wave1(pixels,num_pixels)  # legacy generator shoe-horned in.
    while True:
        next(iter)  # no return values
        yield (pixels,tree_speed.value)
        # no sleep here, it happens in wave1() 

if __name__=='__main__':
   test_loop(generator) 
     
