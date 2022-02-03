from random import random

def is_point_inside_unit_circle(p):
    x = random()
    y = random()
    return 1 if x*x+y*y<1 else 0
