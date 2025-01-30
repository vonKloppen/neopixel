#!/bin/env python3

import board, neopixel
from time import sleep

leds = 16

# PIN 18
pix = neopixel.NeoPixel(board.D18, leds)

# Reset all leds
def reset():
    for ledNumber in range(0, leds):
        pix[ledNumber] = (0, 0, 0)

def setLed(n, x, y, z):
    pix[n] = (x,y,0)

reset()

for a in range(0,leds):
    pix[a] = (255, 0, 0)

currentLed = 0
count = 1

while count <= 10:
    if currentLed == 16:
        currentLed = 0
        count += 1

    pix[currentLed] = (0, 255, 0)
    pix[currentLed - 1] = (255, 0, 0)
    currentLed += 1
    sleep(0.01)

reset()

