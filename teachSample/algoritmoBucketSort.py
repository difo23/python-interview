from random import randrange
from time import time
"""
Genero 5000 datos de prueba entre 0 1000 aleatoriamente.
"""
datosPrueba= []
for valor in range(5000):
    datosPrueba.append(randrange(1000))  

#print(datosPrueba)


def bucket_sort(seq):
   # tamListSeq = seq.__len__()
   # digitos= str(tamListSeq).__len__()
    if seq.__len__() <= 1: 
        return seq
    biggest = 0
    for valor in seq:
       if biggest <= valor:
           biggest = valor
    digitos = str(biggest).__len__()
    out = []
    exponente = 1
    while digitos >= exponente:
        buck=[]
        for valor in seq:
            if valor <= 10**(exponente) and valor >= 10**(exponente-1):
                buck.append(valor)
        out += quicksort(buck)
        
        exponente +=1
    return out
    

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

print "Inicio Prueba de tiempo para 5000 datos en bucket_sort:\n"
start = time()
#print(bucket_sort(datosPrueba))
bucket_sort(datosPrueba)
end = time()
print end-start