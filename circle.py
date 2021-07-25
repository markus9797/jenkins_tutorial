# compitable with python > 3.6

from math import pi
from typing import Union

def calcArea(r: Union[float, int]) -> Union[float, int]:
    return (r**2)*pi

radius = 20

sample_area = calcArea(radius)
print("Radius: {}, Area: ~{:.2f}\n".format(radius, sample_area))