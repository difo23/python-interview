
def valorMaximo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        maxT = valorMaximo(lista[1:])
        if maxT > lista[0]:
            return maxT
        
        else:
            return lista[0]


print(valorMaximo([2, 48, 100, 23, 730, 1, 4]))