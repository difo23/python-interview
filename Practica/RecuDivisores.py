def divisoresNum(numero, divisores = 1):
    if divisores == numero:
        return "sus divisores son:\nY el %d"%(numero)

    elif numero % divisores == 0:
        print("Sus divisores son:\nEl %d" %(divisores))
        return divisoresNum(numero, divisores + 1)

    else:
        return divisoresNum(numero, divisores + 1)

numero = int(input("Introduzca un numero para ver sus divisores: "))
print(divisoresNum(numero))