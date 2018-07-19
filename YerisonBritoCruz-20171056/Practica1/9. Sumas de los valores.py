lista = []
valores = 0
suma = 0
cuadrado = 0
promedio = 0
num = int(input("¿Cúantos valores quieres introducir? "))    # el usuario elige cúantos número quíere introducir

for contador in range(0, num):
    promedio += 1
    valores = int(input("Introduce el valor %d :" % (contador+1)))
    lista.append(valores)
    suma = suma+lista[contador]
    cuadrado = cuadrado+(lista[contador]**2)

promedio = suma/promedio

print("La suma de los %d valores es igual a: %d \nLa suma de los cuadrado es igual: %d " % (valores, suma, cuadrado))
print("El Valor maximo introducido es igual a %d \nEl valor minimo introducido es igual a: %d"
      "\nEl promedio es igual a: %d" % (max(lista), min(lista), promedio))



