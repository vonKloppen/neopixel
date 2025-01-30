#!/bin/env python3

import board, neopixel
from time import sleep
from random import randint

leds = 16

# PIN 18
pix = neopixel.NeoPixel(board.D18, leds)

# Reset all leds
def reset():
    for ledNumber in range(0, leds):
        pix[ledNumber] = (0, 0, 0)

while True:

    for a in range(0, leds):
        pix[a] = (randint(0, 255), randint(0, 255), randint(0, 255))

    sleep(0.1)

reset()
