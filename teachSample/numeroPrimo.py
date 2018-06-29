def es_primo(numero):
    """
    Funcion que determina si un numero es primo
    Tiene que recibir el numero entero
    """
    # Para que un numero sea primo, unicamente tiene que dividirse dos veces:
    #   1 - divisible entre 1
    #   2 - divisible entre el mismo
    # En este bucle, empezamos por el dos hasta un numero anterior a el, por lo
    # que si en el bucle, alguna vez se divide el numero, quiere decir que no es
    # primo
    for i in range(2,numero):
        if (numero%i)==0:
            # es divisible
            return False
    return True
 
 # fin de la funcion es primo

try:
    numero = int(input("inserta un numero: "))
    if numero==0:
        print("tu numero es 0 introduce un numero n>0")
    if es_primo(numero):
        print ("\nEl numero %s es primo" % numero)
    else:
        print ("\nEl numero %s NO es primo" % numero)
except:
    print ("\nEl numero tiene que ser entero")