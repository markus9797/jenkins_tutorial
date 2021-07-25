# test_circle.py
# run with python3.9 -m unittest <test_circle.py>

from unittest import TestCase
from circle import calcArea
from math import pi

class CircleTests(TestCase):
    def test_area(self):
        self.assertAlmostEqual(calcArea(1), pi)