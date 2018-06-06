
from random import randrange
from time import time

"""
Genero 50 datos de prueba entre 0 1000 aleatoriamente.
"""

datosPrueba= []
for valor in range(50000):
    datosPrueba.append(randrange(1000))

# print(datosPrueba)


def heapSort(lst):
    ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''
    # in pseudo-code, heapify only called once, so inline it here
    for start in range((len(lst)-2)/2, -1, -1):
      siftdown(lst, start, len(lst)-1)
 
    for end in range(len(lst)-1, 0, -1):
      lst[end], lst[0] = lst[0], lst[end]
      siftdown(lst, 0, end - 1)
    return lst
 
def siftdown(lst, start, end):
  root = start
  while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
             break




print "Inicio Prueba de tiempo para 5000 datos en heapSort:\n"
start = time()
# print(heapSort(datosPrueba))
heapSort(datosPrueba)
end = time()
print end-start