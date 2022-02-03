import numpy as np
from time import time
from pyspark.sql import SparkSession
from operator import add
from .points import is_point_inside_unit_circle

def pi_estimator_spark(n):
    spark = SparkSession.builder.appName('pi-estimator').getOrCreate()
    sc = spark.sparkContext
    t = time()
    nin = sc.parallelize(range(0,n)).map(is_point_inside_unit_circle).reduce(add)
    print("Estimation de pi avec Spark : %f" % (4.0 * nin / n))
    print("--- %s secondes ___" %(time()-t))
    spark.stop()