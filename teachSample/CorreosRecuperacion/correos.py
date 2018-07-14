from random import randrange
from time import time
from collections import defaultdict

"""
Genero 1000000 datos de prueba entre 0 1000000 aleatoriamente.
"""
#Creo un arreglo para guardar los arreglos sin ordenar producidos aleatoriamente.
correosSinOrdenar= []

# [{19:[233]},{20:[333]}, {19:[36]}, {19:[233]}]
#{19:233}

for valor in range(40):# repito la creacion de correos hasta un millon
    idCiudad = randrange(1,21) #creo un idCiudad aleatoriamente entre 1 a 20
    idDireccion = randrange(1, 1000001) #un idDireccion aleatorio entre 1 a un millon
    correo={} #creo un diccionario vacio para guardar el correo o limpio el anterior
    correo[idCiudad]= idDireccion #creo el primer correo 
    correosSinOrdenar.append(correo) #guardo el correo creado como un elemento nuevo

print(correosSinOrdenar)

# bucket_sort
# correosOrdenadosPorCasilleros
# {10: [911002,156430,825009, 39591, 485167]}
# {4: [81086,444373,78280,361745]}

# [39591,]

def bucket_sort(seq):

    if seq.__len__() <= 1: 
         return seq
    buckNoOrdenado = defaultdict(list)
    buckOrdenado = defaultdict(list)
    for correoBuck in seq:
        for k, v in correoBuck.items() :
            buckNoOrdenado[k].append(v)
    for k , v in buckNoOrdenado.items():
        buckOrdenado[k]= quicksort(v)

    return buckOrdenado 

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


print ("Inicio Prueba de tiempo para 10 datos en bucket_sort:\n")

start = time()
print(bucket_sort(correosSinOrdenar))
end = time()
print( end-start)


