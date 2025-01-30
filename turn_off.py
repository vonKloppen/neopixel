#!/bin/env python3

import board, neopixel
from time import sleep

leds = 16

# PIN 18
pix = neopixel.NeoPixel(board.D18, leds)

# Reset all leds
for ledNumber in range(0, leds):
    pix[ledNumber] = (0, 0, 0)

