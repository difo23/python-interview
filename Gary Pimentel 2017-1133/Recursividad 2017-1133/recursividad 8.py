def trigo(n):
    if n == 0:
        return 0
    else:
        return 2 ** trigo(n-1)

print(trigo(64))

#este programa es un ejemplo de que la recursividad tiene limites
#este programa hace bom bom a la pc