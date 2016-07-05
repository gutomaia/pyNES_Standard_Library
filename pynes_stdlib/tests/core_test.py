import unittest

from unittest import skip

from pynes.asm import *
from pynes_stdlib.core import wait_vblank
from pynes_stdlib.core import clear_memory

class CoreTest(unittest.TestCase):

    def test_waitvblank_inner_code(self):
        expression =  (
            BIT + '$2002' +
            RTS
        )
        actual = str(expression)
        expected = '\n'.join([
                'BIT $2002',
                'RTS'
            ]) + '\n'
        self.assertEquals(actual, expected)

    @skip
    def test_waitvblank(self):
        expression = wait_vblank()
        actual = str(expression)
        expected = '\n'.join([
                'wait_vblank:',
                'BIT $2002',
                'RTS'
            ]) + '\n'
        self.assertEquals(actual, expected)

    def test_instruction_plus_waitvblank(self):
        expression =  (
            SEI +
            wait_vblank()
        )

        actual = str(expression)
        expected = '\n'.join([
                'SEI',
                'wait_vblank:',
                'BIT $2002',
                'BPL wait_vblank'
            ]) + '\n'
        self.assertEquals(actual, expected)

    @skip
    def test_waitvblank_called_twice(self):
        expression =  (
            wait_vblank() +
            LDA + 00 +
            wait_vblank()
        )

        actual = str(expression)
        expected = '\n'.join([
                'wait_vblank:',
                'BIT $2002',
                'BPL wait_vblank',
                'wait_vblank:',
                'BIT $2002',
                'BPL wait_vblank'

            ]) + '\n'
        self.assertEquals(actual, expected)

    def test_clear_memory(self):
        expression = clear_memory()
        actual = str(expression)
        expected = '\n'.join([
                'clear_memory:',
                'LDA #0',
                'STA $0000, x',
                'STA $0100, x',
                'STA $0200, x',
                'STA $0400, x',
                'STA $0500, x',
                'STA $0600, x',
                'STA $0700, x',
                'LDA #254',
                'STA $0300, x',
                'INX',
                'BNE clear_memory'
            ]) + '\n'


        self.assertEquals(actual, expected)

