print("Sumar numeros metodo de Gauss ")     
contador = 1
while contador >= 1:

    numero = int(input("Introduce un numero"))
    gauss = (numero*(numero+1))/2

    print("La suma de los numeros entre 0 y %d es igual a: \n %d " % (numero, gauss))
    

    if numero == 1:
        numero += 1

    else:
        contador -= 1



