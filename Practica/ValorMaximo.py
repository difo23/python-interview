primer_numero = int(input("Introduzca el primer numero: "))
segundo_numero = int(input("Introduzca un segundo numero: "))

def MaxValue(n,m):
    if n > m:
        print("El numero de mayor valor es: %s" %(n))
    else:
        print("El numero de mayor valor es: %s" %(m))

MaxValue(primer_numero, segundo_numero)
print("Fin del Programa")