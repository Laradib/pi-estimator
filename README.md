# Projet pi-estimator : 
Ce projet consiste à donner une approximation de 'pi' à l'aide de deux méthodes 'spark' et 'numpy' après avoir simuler n points qui se trouvent dans un carré contenant le cercle unité. 
# Nb :
Pour exécuter le programme, il faut tout d'abord ouvrir le terminal et faire la commande suivante: git clone %%%%%%%%%%%%%%%LINK%%%%%, puis bien se mettre dans le dossier du projet 'pi-estimator' et ensuite taper python pi-estimator.py ou bien simplement faire sh main.sh
# Résultats selon spark et numpy :
On a écris deux fonctions 'pi-estimator-spark' et 'pi-estimator-numpy', qui prennent un nombre n et permettent de simuler un point p de coordonnées x et y pour savoir ensuite s'il est à l'intérieur ou à l'extérieur du cercle. Voici les résultats trouvés pour 100 000 et 1 000 000 points. 

<img width="506" alt="4" src="https://user-images.githubusercontent.com/94738217/152570489-4e26cdea-aa44-485b-a09a-f7acbe16fa84.png">

# Pour n = 100 000:                                             
<img width="348" alt="1" src="https://user-images.githubusercontent.com/94738217/152568948-96eb62ea-27db-4793-b548-a891398ed2b4.png">   

# Pour n = 1 000 000: 
<img width="347" alt="2" src="https://user-images.githubusercontent.com/94738217/152569025-3e6c8284-511b-442d-a17d-b2cc8e8b7250.png">

Si on remarque bien les résultats obtenus, on trouve que pour 100 000 nympy est plus précise que spark. On a trouvé un écart de 0.038 avec numpy alors qu'avec spark l'erreur est de 0.257 donc plus grand. Mais pour 1 000 000, c'est totalement l'inverse. Avec spark il y a plus de précision dans la valeur de pi qu'avec numpy. De plus, on remarque que le temps d'éxécution avec numpy est toujours mieux. Dans les deux cas, numpy est plus rapide et a une vitesse d'exécution plus élevée que celle de spark.
