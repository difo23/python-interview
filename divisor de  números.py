numero = int(input("Introduzca un número:"))
divisores = 0

if numero > 0:
   for contador in range(numero, 0, -1):
     if numero % contador == 0:
       divisores = contador
       print(divisores)

else:
    print("Error, introdujo un número negativo")
