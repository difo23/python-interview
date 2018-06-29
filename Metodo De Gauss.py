print("Sumador de números")
contador = 1
# metodo gauss = n*n+1/2

while contador >= 1:

    acceder = int(input("Introduzca un número entero "))
    metodoGauss = (acceder*(acceder+1))/2

    print("La suma de los números comprendidos entre 0 y %d es igual a: \n %d " % (entrada, gauss))
    acceder = int(input("¿quiere seguir sumando? \n 1=si \n 0=no "))
    
if acceder == 1:
   acceder += 1

else:
     contador -= 1

print("Nos vemos")



