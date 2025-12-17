# Copyright 2025 R. Gary Cutbill
# All rights reserved

'''Montage decorator
This decorator loads other decorators for a period of time and then
switches them periodically.
'''

import pdb
from time import sleep
from coords import *
import datetime
from importlib import import_module
from common_utils import test_loop

modules=[ '_startup', 'chase1', 'simple_xmas', 'wave1',  'neotest2', 'bluesparkle', '_startup', 'counter-rotate' ]
 
def generator(pixels,tree_speed,tree_angle,form_data):
    modlist=[]
    for i in modules:
        # don't reload the montage(this) module
        # if the module list is dynamic, this might be important later
        if i=='montage':  
           continue
        try:
            # Try to import the candidate module, skip it on an exception
            mod=import_module(i)
        except:
            continue
        modlist.append(mod)

    period=datetime.timedelta(minutes=1) # how long to run each module
    for curmod in modlist:
        tree_speed.value=0
        try: # get the generator function, bail out on an exception
            it=curmod.generator(pixels,tree_speed,tree_angle,form_data)
            now=datetime.datetime.now()
            future=now+period
    
            while datetime.datetime.now()<future:
               (pixels,speed) = next(it)
               yield (pixels,tree_speed.value)
        except:
            print(f'{curmod} failed')
            continue

if __name__=='__main__':
   test_loop(generator) 
