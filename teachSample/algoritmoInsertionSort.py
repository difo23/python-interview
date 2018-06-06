
from random import randrange
from time import time
"""
Genero 50 datos de prueba entre 0 1000 aleatoriamente.
"""
datosPrueba= []
for valor in range(50000):
    datosPrueba.append(randrange(1000))

def insertion_sort(l):
    for i in xrange(1, len(l)):
        j = i-1 
        key = l[i]
        while (l[j] > key) and (j >= 0):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key


print "Inicio Prueba de tiempo para 5000 datos en insertion_sort:\n"
start = time()
# print(insertion_sort(datosPrueba))
insertion_sort(datosPrueba)
end = time()
print end-start