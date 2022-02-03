import numpy as np
from time import time
from .points import is_point_inside_unit_circle

def pi_estimator_numpy(n):
    t = time()
    nin = 0
    for i in range (n):
        pt = is_point_inside_unit_circle(0)
        if pt == 1 :
            nin = nin + 1
    pi = 4*nin/n
    print("Estimation de pi avec numpy : %f" %pi)
    print("--- %s secondes ___" %(time()-t))
    