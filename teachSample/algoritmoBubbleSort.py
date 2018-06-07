
from random import randrange
from time import time
"""
Genero 50 datos de prueba entre 0 1000 aleatoriamente.
"""

datosPrueba = [16,14,10,8,7,9,3,2,4,1]
# datosPrueba= []
# for valor in range(50000):
#     datosPrueba.append(randrange(1000))
# Este algoritmo es O(n^2)

def bubbleSort(seq):
    if seq.__len__() <= 1: 
        return seq
    
    seqSize = seq.__len__()
    aux = 0
    for i in range(1,seqSize):
        for j in range(0, seqSize-i):
            if seq[j] > seq[j+1]:
                aux = seq[j]
                seq[j] = seq[j+1]
                seq[j+1] = aux     
    return seq




print "Inicio Prueba de tiempo para 5000 datos en bubbleSort:\n"
start = time()
# print(bubbleSort(datosPrueba))
bubbleSort(datosPrueba)
end = time()
print end-start