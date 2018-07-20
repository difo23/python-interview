def suma(lista):
    if lista.__len__() == 1:
        return lista[0]
    else:
        return lista[0] + suma(lista[1:])


def Cuadrado(lista):
    if lista.__len__()==1:
        return lista[0]**2
    else:
        return lista[0]**2 + Cuadrado(lista[1:])


def maximo(list):
    if len(list) == 1:
        return list[0]
    else:
        m = maximo(list[1:])
        return m if m > list[0] else list[0]


numeros = [1,2,3,4,5,6,7,8,9 ]
numeros2 = [875, 695, 321, 474, 654, 6574]

print("la Suma de %s es igual a: %d \nLa suma de cuadrado es igual a: %d \nSu Valor maximo es igual a %d"
      "\nEl promedio es igual a %d " % (numeros, suma(numeros), Cuadrado(numeros), max(numeros),
                                        (suma(numeros)/len(numeros))))
