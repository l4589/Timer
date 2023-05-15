# Goes with programming lessons on: https://soriki.com/pico/
# Lensyl Urbano

import board
import neopixel
import time
import math
pixels = neopixel.NeoPixel(board.GP0, 12)

for i in range(10*5):
    n=math.floor(i/5)
    for j in range(10):
        if j>n:
            pixels[j]=(0,200,0)
        else:
            pixels[j]=(0,0,0)
    print (i,n)
    time.sleep (1)
    
for i in range(5*5):
    n=math.floor(i/5)
    for j in range(5):
        if j>n:
            pixels[j]=(200,200,0)
        else:
            pixels[j]=(0,0,0)
    print (i,n)
    time.sleep (1)
        
        



