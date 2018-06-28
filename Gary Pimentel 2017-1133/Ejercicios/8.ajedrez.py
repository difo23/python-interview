def ajedrez(n):
    trigo = 0
    resultado = 0
    for i in range(0,n,1):
        resultado = i**2
        trigo += resultado
        
    return trigo

print(ajedrez(65))