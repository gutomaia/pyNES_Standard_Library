from pynes.lib import asm_def
from pynes.asm import *

@asm_def
def wait_vblank():
    return (
        BIT + '$2002' +
        wait_vblank()
    )

@asm_def
def clear_memory():
    return (
        LDA + 00 +
        STA + ('$0000', X) +
        STA + ('$0100', X) +
        STA + ('$0200', X) +
        STA + ('$0400', X) +
        STA + ('$0500', X) +
        STA + ('$0600', X) +
        STA + ('$0700', X) +
        LDA + '$FE' +
        STA + ('$0300', X) +
        INX +
        BNE clear_memory()
    )

@asm_def
def infinity_loop():
    return JMP + infinity_loop()
