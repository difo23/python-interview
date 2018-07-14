cuadricula = 2
trigo = 0

for tablero in range(0, 64):
    cuadricula = 2 ** tablero
    trigo = trigo+cuadricula
    print("%d granos de trigo por %d cuadricula " % (cuadricula, (tablero+1)))

print("Un total de %d granos de trigos " % trigo)

