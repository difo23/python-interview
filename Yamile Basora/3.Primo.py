def primo(numero,modulo=2):
    if numero%modulo==0 and numero>2:
        return False
    elif modulo>numero/2:
        return True
    else:
        return primo(numero,modulo+1)

cantidadPrimos=0
numero=0
cantidadNumeros=int(input("dijite la cantidad de numero que quieres introducir"))

for i in range (cantidadNumeros):
    numero=int(input("introduce el numero%d"%(i+1)))
    if primo (numero):
        cantidadPrimos +=1


print("son %d primos"%cantidadPrimos)