from random import randrange
from time import time
"""
Genero 5000 datos de prueba entre 0 1000 aleatoriamente.
"""
datosPrueba= []
for valor in range(5000):
    datosPrueba.append(randrange(1000))  

#print(datosPrueba)

def quicksort(seq):
    if seq.__len__() <= 1: 
        return seq
    lo, pi, hi = partition(seq)
    return quicksort(lo) + [pi] + quicksort(hi)

def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi

print "Inicio Prueba de tiempo para 5000 datos en quicksort:\n"
start = time()
#print(quicksort(datosPrueba))
quicksort(datosPrueba)
end = time()
print end-start