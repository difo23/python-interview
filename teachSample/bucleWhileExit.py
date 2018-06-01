from random import randrange

adivina = randrange(100)
intentosCorrectos = 0
intentosIncorrectos = 0
passwordInt = 1

print("Adivina el numero 0-100, intentos 5 de 5")

while True and intentosCorrectos < 5 and intentosIncorrectos < 5:
    
    numero = input("introduce el numero:")
    numeroInt = int(numero)
 
    if numeroInt == adivina:
        intentosCorrectos +=1
        print("Es correcto %d. Cambio el numero \n" %numeroInt)
        adivina = randrange(100)

    elif passwordInt == 0:
        exit()
    else:
        intentosIncorrectos+=1
        print("El numero era %d " %adivina)
        print("Cambio el numero \n")
        adivina = randrange(100)
        print("Sigue intentandolo")

    print("Intentos correctos %d intentos incorrectos %d vuelve a tratar . \n" %(intentosCorrectos, intentosIncorrectos))

    password = input("Quieres salir despues de un ultimo intento?introduce  0 sino intoduce 1:")
    passwordInt = int(password)
    
if intentosCorrectos > intentosIncorrectos:
    print("Ganas!")
else:
    print("Pierdes no tienes mas intentos!")

