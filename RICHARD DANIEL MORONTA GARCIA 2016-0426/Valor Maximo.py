numero1 = int(input("Introduce el primer numero "))
numero2 = int(input("Introduce el segundo numero "))


def maxVal(primernumero, segundonumero):

    if primernumero > segundonumero:
        print(" El mayor valor es primernumero %d " % primernumero)
    else:
        print(" El mayor valor es segundonumero %d " % segundonumero)


maxVal(numero1, numero2)
