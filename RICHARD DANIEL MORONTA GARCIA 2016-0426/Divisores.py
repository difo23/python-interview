numero = int(input("Introduce un numero"))
divisores = 0

if numero > 0:
    for contador in range(numero, 0, -1):
        if numero % contador == 0:
            divisores = contador
            print(divisores)

else:
    print("Error no puede introducir un numero negativo")
