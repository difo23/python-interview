#Metodo con str
def cdig(n, d):
    numeroStr = str(n)
    conteo = 0
    digito = str(d)
    
    for valor in  numeroStr:
        if valor == digito :
            conteo +=1

    return conteo


print(cdig(124783191, 1))
