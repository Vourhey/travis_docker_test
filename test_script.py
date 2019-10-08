#!/usr/bin/env python3

import unittest
from script import say_hello

class TestScript(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(say_hello("VAdim"), "Hello, Vadim")

    def test_hello_2(self):
        self.assertEqual(say_hello("Alexander"), "Hello, Alexander")


if __name__ == "__main__":
    unittest.main()

