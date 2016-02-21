"""Core Functions"""

from pynes.lib import asm_def
from pynes.asm import *

@asm_def
def wait_vblank():
    """Wait until vblank is triggered.

    Stops CPU from running by looping instructions
    until vblank is checked.
    """

    return (
        BIT + '$2002' +
        BPL + wait_vblank()
    )

@asm_def
def clear_memory():
    """Clear entire RAM space

    You must set the entire RAM space on system
    initalization. On the actual hardware, it usually
    start with some dirty on memory.
    """

    return (
        LDA + 0 +
        STA + ['$0000', X] +
        STA + ['$0100', X] +
        STA + ['$0200', X] +
        STA + ['$0400', X] +
        STA + ['$0500', X] +
        STA + ['$0600', X] +
        STA + ['$0700', X] +
        LDA + 0xfe +
        STA + ['$0300', X] +
        INX +
        BNE + clear_memory()
    )

@asm_def
def infinity_loop():
    """Loop Forever

    On initialization, you will need to stop the CPU counter
    from fetching more instructions.
    """
    return JMP + infinity_loop()
