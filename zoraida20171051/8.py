#Inventor Ajedrez

casillas_tablero = 64

for c in range(casillas_tablero+1):

    granos = 2**c

    print("El inventor del tablero solicitó",granos,"granos de trigo")

#Cálculo

granos_por_kilo = 25000 #cantidad de granos por kilo

Kilogramos = granos / granos_por_kilo #convertir a Kg

toneladas = Kilogramos/ 1000 #convertir a toneladas

print("El peso total es %4.2f toneladas" %toneladas)