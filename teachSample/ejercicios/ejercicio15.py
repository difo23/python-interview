# 15. Hacer una función cdig(n, d), se desea que dicha funcion retorne las veces que el dígito d
# esta contenido en el número n. Por ejemplo: cdig(1241, 1) = 2, cdig(28858, 8)=3.


#Metodo con str
def cdig(n, d):
    numeroStr = str(n)
    conteo = 0
    digito = str(d)
    
    for valor in  numeroStr:
        if valor == digito :
            conteo +=1

    return conteo


#Metodo con %
def cdigModulo(n, d):
    conteo = 0
    while n > 0:
        actual = n%10
        if actual == d:
            conteo+=1
        n = n//10
    

    return conteo


print(cdig(1241, 1))

print(cdig(28858, 8))

print(cdigModulo(1241, 1))

print(cdigModulo(28858, 8))