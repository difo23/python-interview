def mayorValor(mayor):
 numero = 0
 if (numero >= 1):

    if valor == 1:
        valor += 1
        
    if numero < 1:
        valor = mayor * mayorValor(mayor-1)
        return
    
valor = int(input("Introduce el valor n "))
valor2 = int(input("Introduce el valor m "))


def maxVal(n, m):

    if n > m:
        print(" El mayor valor es n %d " % n)
    else:
        print(" El mayor valor es m %d " % m)


maxVal(valor, valor2)



