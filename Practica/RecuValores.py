def sumVal(numeros):
    if numeros.__len__() == 1:
        return numeros[0]
    else:
        return numeros[0] + sumVal(numeros[1:])

def sumCuad(numeros):
    if numeros.__len__()==1:
        return numeros[0]**2
    else:
        return numeros[0]**2 + sumCuad(numeros[1:])

def valorMaximo(numeros):
    if len(numeros) == 1:
        return numeros[0]
    else:
        maxT = valorMaximo(numeros[1:])
        if maxT > numeros[0]:
            return maxT
        
        else:
            return numeros[0]

lista = [1, 42, 23, 8, 10, 3, 25]
promedio = sumVal(lista) // len(lista)

print("""La Suma de todos los elementos de %s es %s
La Suma de los cuadrados es %s
El elemento con mayor valor es %s
El Promedio de los numeros en la lista es %s""" %(lista, sumVal(lista), sumCuad(lista), valorMaximo(lista), promedio))