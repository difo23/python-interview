lista = []
valores = 0
sum = 0
cuadrado = 0
prom = 0
numero = int(input("¿Cúantos valores desea introducir? "))   

for contador in range(0, numero):
    promedio += 1
    valores = int(input("Introduce el valor %d :" % (contador+1)))
    lista.append(valores)
    sum = suma+lista[contador]
    cuadrado = cuadrado+(lista[contador]**2)

promedio = sum/prom

print("La suma de los %d valores es igual a: %d \nLa suma de los cuadrado es igual: %d " % (valores, suma, cuadrado))
print("El Valor maximo introducido es igual a %d \nEl valor minimo introducido es igual a: %d"
      "\nEl promedio es igual a: %d" % (max(lista), min(lista), promedio))



