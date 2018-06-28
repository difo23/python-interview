print("Divisores de un número Digitado")
numero = int(input("Escriba un número entero mayor que cero: "))

if numero <= 0:
    print("Error! Se ha pedido un  número Mayor que 0")
else:
    print("Los divisores del Número son ")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)
