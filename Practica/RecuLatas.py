def triangulo(nivel):
    if nivel <= 1:
        return nivel
    else:
        return triangulo(nivel - 1) + 2

def latas(lata, aux = 0):
    if lata < triangulo(aux):
        return "Podemos hacer %d niveles con %d y sobran %d latas" %(aux, lataC, lata)
    else:
        return latas(lata-triangulo(aux+1), aux+1)

lataC = int(input("Cuantas latas posee?\n"))
print(latas(lataC))