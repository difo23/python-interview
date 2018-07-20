print("primeraGrafica")


def grafica(lista, contador = 6):
    if contador == 1:
        return lista[0]
    else:
        print(lista[:contador:])
        return grafica(lista, contador-1)


print(grafica([1, 2, 3, 4, 5, 6]))

print("\n")
print("segundaGrafica")


def segundaGrafica(lista, contado=1):

    if contado >= 9:
        return lista
    else:
        print(lista[0:contado])
        return segundaGrafica(lista, contado + 2)
        

print(segundaGrafica([1, 2, 3, 4, 5, 6, 7, 8, 9]))

print("\n")
print("terceraGrafica")


def terceraGrafica(lista, contador=1):
    if contador >= 7:
        return lista
    else:
        print(lista[0:contador])
        return terceraGrafica(lista, contador+2)


print(terceraGrafica([1, 2, 3, 4, 5, 6, 7]))

print(grafica([1, 2, 3, 4, 5, 6, 7]))
