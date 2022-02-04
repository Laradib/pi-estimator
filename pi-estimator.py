from pyspark import SparkContext,SparkConf
from random import random                      # les packages
from time import time
import numpy as np
import math

conf = SparkConf().setAppName("piestimator").setMaster("local")
sc = SparkContext(conf=conf)
n=1000000

def is_point_inside_unit_circle(n):
    x, y = random(), random()    # pour simuler deux points  x et y
    return 1 if x*x + y*y < 1 else 0  # pour vérifier si ces deux points sont dans le cercle

def pi_estimator_spark(n):    
    count = sc.parallelize(range(n)).map(is_point_inside_unit_circle).reduce(lambda a,b : a+b)
    pi_est = 4*count/n        
    return count, pi_est
  
def pi_estimator_numpy(n):    
    count = np.arange(n)    
    for i in range(n) :
        count[i] = is_point_inside_unit_circle(0)       
    tot = np.sum(count)        
    pi_est = 4*tot/n        
    return tot, pi_est

#Calcul avec Spark
t_init_S = time() 
(nb_pts_S, pi_est_S) = pi_estimator_spark(n) 
tmp_S = np.round(time()-t_init_S,6)
Ec_perc_S = np.abs(round(100-(pi_est_S/math.pi)*100,4)) 

print("")
print("Spark")
print("Parmis les",n,"points,",nb_pts_S, "sont dans le cercle.")
print("")
print("Une approximation de Pi est de", pi_est_S, ".")
print("")
print("Le temps d'execution de l'algorithme avec Spark est de",tmp_S,"secondes.")
print("")
print("L'erreur est de", Ec_perc_S, "%")
print("")

#Calcul avec Numpy
t_init_N = time() 
(nb_pts_N, pi_est_N) = pi_estimator_numpy(n)
tmp_N = np.round(time()-t_init_N,6) # pour donner le temps de calcul
Ec_perc_N = np.abs(round(100-(pi_est_N/math.pi)*100,4))

print("Numpy")
print("Parmis les",n,"points,",nb_pts_N, "sont dans le cercle.")
print("")
print("Une approximation de Pi est de", pi_est_N, ".")
print("")
print("Le temps d'execution de l'algorithme avec Numpy est de",tmp_N,"secondes.")
print("")
print("L'erreur est de", Ec_perc_N, "%")

sc.stop() # pour fermer le SparkContext
