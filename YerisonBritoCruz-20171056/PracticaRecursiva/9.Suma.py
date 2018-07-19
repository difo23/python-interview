def sumaValores(lista):
    if lista.__len__() == 1:
        return lista[0]
    else:
        return lista[0] + sumaValores(lista[1:])


def sumaCuadrado(lista):
    if lista.__len__()==1:
        return lista[0]**2
    else:
        return lista[0]**2 + sumaCuadrado(lista[1:])


def max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = max(list[1:])
        return m if m > list[0] else list[0]


datos = [1,2,3,4,5,6,7,8,9 ]
datosB = [875, 695, 321, 474, 654, 6574]

print("la Suma de %s es igual a: %d \nLa suma de cuadrado es igual a: %d \nSu Valor maximo es igual a %d"
      "\nEl promedio es igual a %d " % (datos, sumaValores(datos), sumaCuadrado(datos), max(datos),
                                        (sumaValores(datos)/len(datos))))
