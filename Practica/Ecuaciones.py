import math
print("Resolvamos una ecuacion de la forma ax^2+bx+c")

def ecuCuad(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)

    comprobacion = (b**2) - (4*a*c)      
    if comprobacion == 0:

        solucion = (-b) / 2*a
        print("La solucion de %sx^2 %sx %s es: %.2f " % (a, b, c, solucion))

    elif comprobacion > 0:

        comprobacion = math.sqrt(comprobacion)

        solucion = (-b + comprobacion) / (2 * a)
        solucion_2 = (-b - comprobacion) / (2 * a)

        if solucion > 0 and solucion_2 > 0:
            print("%sx^2 %sx %s posee dos soluciones: %.2f y %.2f" %(a, b, c, solucion, solucion_2))
        elif solucion > 0:
            print("La solucion para %sx^2 %sx %d es: %.2f  " %(a, b, c, solucion))
        else:
            print("La solucion para %sx^2 %sx %d es: %.2f  " %(a, b, c, solucion_2))
    else:
        print("Su solucion no esta definida en el conjunto de los numeros reales")

ecuCuad(input("Escriba el valor de A: "), input("Escriba el valor de B: "), input("Escriba el valor de C: "))
print("Fin del Programa")