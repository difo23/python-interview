contador = 1

while contador >= 1:

    a = int(input("Introduce un número entero "))
    b = (a*(a+1))/2

    print("La suma de los números comprendidos entre 0 y %d es igual a: \n %d " % (a, b))

    if a == 1:
        a += 1

    else:
        contador -= 1

print("terminado")



