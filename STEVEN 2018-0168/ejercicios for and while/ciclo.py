grafica = int(input("Que tipo de grafico quieres\n1.para decreciente\n2.para ascendente\n3.para semidecreciente\n: "))
contador = 6
contador1 = 1
contador2 = 1
if grafica == 1:
    while contador != 0:
        print("*" * contador)
        contador -= 1
if grafica == 2:
    while contador1 < 10:
        print("*" * contador1)
        contador1 += 2
if grafica == 3:
    while contador2 < 10:
        print("*" * contador2 ) 
        contador2 += 2     
    while contador2 > 0:
        contador2 -= 2
        print("*" * contador2)    
      
