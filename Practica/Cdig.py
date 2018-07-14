print("Cavemos en numero para saber cuantas veces se repite dentro de otro!")
def Cdig(n, d):   
    numero = str(n)
    numero_2 = str(d)
    contador = 0

    for i in numero:
        if i == numero_2:
            contador +=1

    return contador

print(Cdig(input("Introduzca el digito: "), input("Introduzca el digito del que quiere ver las repeticiones: ")))