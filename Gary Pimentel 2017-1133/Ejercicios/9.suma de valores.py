numeros = []
numero = 0
suma = 0
cuadratico = 0
promedio = 0
for conteo in range(10):
    numero = int(input("Digite el %d numero para la lista: " %(conteo+1)))
    numeros.append(numero)
    suma = suma+numeros[conteo]
    cuadratico += (numeros[conteo]**2)
promedio = suma/10
print("Esta es la lista %d" %numero)
print("La suma entre ellos seria un total de %d" %suma)
print("La suma entre ellos al cuadrado seria un total de %d" %cuadratico)
print("El promedio de esta lista seria %d" %promedio)