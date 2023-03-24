# Place this in the root directory of the CIRCUITPY drive
# This configuration will only type the alphabet that is 
# convienet for testing purposes
#
# Visit http://kmkfw.io/ for further configuration guidance

print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()


keyboard.col_pins = (board.D4, board.D5, board.D6, board.D7)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D,
     KC.E, KC.F, KC.G, KC.H,
     KC.I, KC.J, KC.K, KC.L,
     KC.M, KC.N, KC.O, KC.P]
]

if __name__ == '__main__':
    keyboard.go()