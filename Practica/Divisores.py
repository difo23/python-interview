print("Vamos a ver los divisores de un numero")
numero = int(input("Introduzca dicho numero: "))
divisores = 0

if numero > 0:
    for i in range(numero, 0, -1):
        if numero % i == 0:
            divisores = i
            print(divisores)
else:
    print("El numero introducido no es valido!")
print("Fin del Programa")