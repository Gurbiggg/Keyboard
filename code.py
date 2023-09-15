print("Starting")
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

split = Split(
    # split_side = SplitSide.LEFT,
    split_flip = True,
    split_type = SplitType.UART,
    data_pin = board.D0,
    data_pin2 = board.D1,
    uart_flip = True,
    use_pio = True,
)

keyboard.modules.append(split)
keyboard.col_pins = (board.D10, board.MOSI, board.MISO, board.SCK, board.A0, board.D2, board.D3)
keyboard.row_pins = (board.D8, board.D7, board.D6, board.D5, board.D4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.NO,   KC.N1, KC.N2,  KC.N3,   KC.N4,   KC.N5,  KC.MINS,     KC.EQL,  KC.N6,  KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.NO,
     KC.TAB,  KC.Q,  KC.W,   KC.E,    KC.R,    KC.T,   KC.LEFT,     KC.UP,   KC.Y,   KC.U,    KC.I,    KC.O,    KC.P,    KC.BSLS,
     KC.LSFT, KC.A,  KC.S,   KC.D,    KC.F,    KC.G,   KC.RGHT,     KC.DOWN, KC.H,   KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,
     KC.LCTL, KC.Z,  KC.X,   KC.C,    KC.V,    KC.B,   KC.DEL,      KC.BSPC, KC.N,   KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT,
     KC.NO,   KC.NO, KC.GRV, KC.LALT, KC.LGUI, KC.SPC, KC.ESC,      KC.ENT,  KC.SPC, KC.RCTL, KC.RALT, KC.LBRC, KC.RBRC, KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()
