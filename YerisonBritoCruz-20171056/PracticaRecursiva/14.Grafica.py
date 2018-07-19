print("Grafica A")


def grafica(lista, contador = 6):
    if contador == 1:
        return lista[0]
    else:
        print(lista[:contador:])
        return grafica(lista, contador-1)


print(grafica([1, 2, 3, 4, 5, 6]))

print("\n")
print("grafica B")


def graficaB(lista, contado=1):

    if contado >= 9:
        return lista
    else:
        print(lista[0:contado])
        return graficaB(lista, contado + 2)
        

print(graficaB([1, 2, 3, 4, 5, 6, 7, 8, 9]))

print("\n")
print("Grafica C")


def graficaC(lista, contador=1):
    if contador >= 7:
        return lista
    else:
        print(lista[0:contador])
        return graficaC(lista, contador+2)


print(graficaC([1, 2, 3, 4, 5, 6, 7]))

print(grafica([1, 2, 3, 4, 5, 6, 7]))
