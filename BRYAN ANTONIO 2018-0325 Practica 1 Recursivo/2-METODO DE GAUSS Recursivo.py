def gauss (n): 
 metodo = 0
 if (metodo >= 1):

    if nuero == 1:
        numero += 1

    if metodo < 1:
        numero = n * gauss(n-1)
        return

numero = int(input("Introduce un número entero "))
proceso = (numero*(numero+1))/2

print("La suma de los números comprendidos entre 0 y %d es igual a: \n %d " % (numero, proceso))
    
print("terminado")



