
casillas = 2
granos = 0
peso = 0.25

for tablero in range(0, 64):
    casillas = 2 ** tablero
    granos = granos+casillas
    print("%s de granos de trigo en la casilla %s" %(casillas, (tablero+1)))

print("Se tiene una cantidad de %s granos en total" % (granos))

peso_total = peso*granos

print("El peso aproximado de los granos es %s gramos" %(peso_total))
print("Fin del Programa")