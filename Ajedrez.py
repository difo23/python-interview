cuadricula = 2
granoTrigo = 0

for tablero in range(0, 64):
    cuadricula = 2 ** tablero
    granoTrigo = granoTrigo+cuadricula
    print("%d granos de trigo por %d cuadricula " % (cuadricula, (tablero+1)))

print("Un total de %d granos de trigos " % granoTrigo)

