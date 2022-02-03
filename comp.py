#!/usr/local/bin/python3

import os 
from functions.numpy_estimator import pi_estimator_numpy 
from functions.spark_estimator import pi_estimator_spark

if __name__=="__main__":
    n = 100000
    pi_estimator_numpy(n)
    pi_estimator_spark(n)
