def divisor(n):
    contador = 0
    dividendo = n
    if dividendo < 0:
        print("error grave del sistema")
        exit()
    for x in range(0,10,1):
        if dividendo % x == 0:
            x = contador
            print(contador)

print(divisor(int(input("Digite el numero: "))))     