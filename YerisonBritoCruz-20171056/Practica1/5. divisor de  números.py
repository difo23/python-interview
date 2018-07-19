number = int(input("Introduce un número"))
divisores = 0

if number > 0:
    for contador in range(number, 0, -1):
        if number % contador == 0:
            divisores = contador
            print(divisores)

else:
    print("Error introdujo un número negativo")
