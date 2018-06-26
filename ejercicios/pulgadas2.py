pulgadas = int(input("cantidad de pulgadas: "))
contadorY = 0
contadorP = 0
while 1 == 1:
    if pulgadas >= 36:
        contadorY += 1
        pulgadas -= 36
    elif pulgadas >= 12:
        contadorP += 1
        pulgadas -= 12
    else:
        print(pulgadas, "pulgadas es igual a",contadorY, "yardas")    
        print(contadorP,"pies")
        print("y sobran",pulgadas,"pulgadas")
        break