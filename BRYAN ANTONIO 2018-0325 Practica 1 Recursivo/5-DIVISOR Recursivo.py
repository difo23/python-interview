def divisor(numero, contador=1):

    if contador == numero:
        return numero

    elif numero % contador == 0:
        print(contador)
        return divisor(numero, contador+1)

    else:
        return divisor(numero, contador+1)


print(divisor(35))
