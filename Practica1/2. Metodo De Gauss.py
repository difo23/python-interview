print("Sumador de números con el metodo de Gauss ")     # metodo gauss = n*n+1/2
contador = 1

while contador >= 1:

    entrada = int(input("Introduce un número entero "))
    gauss = (entrada*(entrada+1))/2

    print("La suma de los números comprendidos entre 0 y %d es igual a: \n %d " % (entrada, gauss))
    entrada = int(input("¿Quíeres seguir sumando? \n si=1 \n no=0 "))
    # El usuario podra sumar más números

    if entrada == 1:
        entrada += 1

    else:
        contador -= 1

print("Hasta pronto")



