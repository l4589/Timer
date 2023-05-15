# Goes with programming lessons on: https://soriki.com/pico/
# Lensyl Urbano

import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.GP0, 12)

c=0
while True:
    c=c+1
    
    time.sleep(1)
    if (c<4*60):
        pixels[0]=(0,200,0)
    elif (c<5*60):
        pixels[0]=(200,200,0)
    else :
        pixels[0]=(200,0,0)
        
