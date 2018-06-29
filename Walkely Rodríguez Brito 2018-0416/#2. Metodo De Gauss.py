print("Sumador de números con el método de Gauss ")  
contador = 1

while contador >= 1:

    entrada = int(input("Introduce un número entero "))
    metodoGauss = (entrada*(entrada+1))/2

    print("La suma de los números comprendidos entre 0 y %d es igual a: \n %d " % (entrada, metodoGauss))
    entrada = int(input("¿Quíeres seguir sumando? \n si=1 \n no=0 "))


    if entrada == 1:
        entrada += 1

    else:
        contador -= 1

print("Hasta pronto")



