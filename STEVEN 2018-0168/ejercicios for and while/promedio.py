suma = 0
promedio = 0
cuadrado = 0
lista = []
for i in range(10):
    numero = int(input("numero: "))
    lista.append(numero)
for i in lista:
    suma = suma + i
print ("la suma de los numeros es:",suma)
for i in lista:
    cuadrado += i ** 2
print("la suma de sus cuadrados es: ",cuadrado)    
promedio = suma / 10
print("el promedio es igual a:",promedio)
print("el maximo es: ")
print(max(lista))
print("el minimo es: ")
print(min(lista))