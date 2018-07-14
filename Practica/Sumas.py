suma = 0
sum_cuadrados = 0
promedio = 0
valores = 0
listado = []
numeros = int(input("Escriba la cantidad de valores a introducir: "))

for conteo in range(0, numeros):
    promedio += 1
    valores = int(input("Introduce el %s numero: " %(conteo+1)))
    listado.append(valores)
    suma = suma+listado[conteo]
    sum_cuadrados = sum_cuadrados+(listado[conteo]**2)

promedio = suma/promedio

print("La suma de los %s valores es: %s\nLa suma de los cuadrados es igual: %s " %(valores, suma, sum_cuadrados))
print("El Numero de Mayor Valor es: %s\nEl Numero de Menor Valor es: %s\n El Promedio es : %s" % (max(listado), min(listado), promedio))
