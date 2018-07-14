import math
print("Resolución de ecuaciones de segundo grado de la forma ax**2+bx+c")


def ecuCuad(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)

    verificador = (b**2) - (4*a*c)        
    if verificador == 0:

        solucion1 = (-b) / 2*a
        print("La solucion para %dX^2 %dX %d es: %.2f " % (a, b, c, solucion1))

    elif verificador > 0:

        verificador = math.sqrt(verificador)

        solucion1 = (-b + verificador) / (2 * a)
        solucion2 = (-b - verificador) / (2 * a)

        if solucion1 > 0 and solucion2 > 0:
            print("%dX^2 %dX %d Tiene dos soluciones positivas: %.2f y %.2f" % (a, b, c, solucion1, solucion2))
        elif solucion1 > 0:
            print("La solucion para %dX^2 %dX %d es: %.2f  " % (a, b, c, solucion1))
        else:
            print("La solucion para %dX^2 %dX %d es: %.2f  " % (a, b, c, solucion2))
    else:
        print("No tiene solucion reales")


ecuCuad(2, 3, -5)
ecuCuad(-5, 13, 6)
ecuCuad(1, -10, 21)
ecuCuad(5, 10, 2)
ecuCuad(-1, 6, -9)
