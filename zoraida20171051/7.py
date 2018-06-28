# Conejo Fibonacci

fibonumero=1
fiultimo=0
fipenultimo=0
print (fibonumero)

for sucesionconteo in range (0,11): # De 0 a 11 porque el vector inicia en 0 entonces de 0 a 11 equivale a 12 meses

    fipenultimo=fiultimo

    fiultimo=fibonumero

    fibonumero=fipenultimo + fiultimo

    print (fibonumero)