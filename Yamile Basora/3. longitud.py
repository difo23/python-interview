
def longitud(pesos,cien=0,cincuenta=0,veinte=0,cinco=0):
    if pesos < 5:
        return "%billetes de 100,%d billetes de 50,%d billetes de 20, %d billetes  de 5, %d peso" % str((cien,cincuenta,veinte,cinco,pesos))
    elif pesos >= 50:
        return longitud(pesos-50,cien,cincuenta+1)
    elif pesos >= 20:
        return longitud(pesos-20,cien,cincuenta,veinte+1)
    else:
        return longitud(pesos-5,cien,cincuenta,veinte,cinco+1)

print(longitud(350))
print(longitud(175))
print(longitud(13577))