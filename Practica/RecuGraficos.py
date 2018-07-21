print("Grafica A")

def graficaUno(lista, cantidad = 6):
    if cantidad == 1:
        return lista[0]
    else:
        print(lista[:cantidad:])
        return graficaUno(lista, cantidad - 1)

print(graficaUno(["*", "*", "*", "*", "*", "*"]))

print("grafica B")

def graficaDos(lista, cantidad = 1):

    if cantidad >= 6:
        return lista
    else:
        print(lista[0:cantidad])
        return graficaDos(lista, cantidad + 1)
        

print(graficaDos(["*", "*", "*", "*", "*", "*"]))

print("Grafica C")

def graficaTres(lista, cantidad = 1):
    if cantidad >= 6:
        return lista
    else:
        print(lista[0:cantidad])
        return graficaTres(lista, cantidad + 2)

print(graficaTres(["*", "*", "*", "*", "*", "*"]) and graficaUno (["*", "*", "*", "*", "*", "*"]))

print("Hagamos tu propio grafico\n")

graficoPropio = []
conversion = graficoPropio

for i in range(0, 6):
    elementos = input("Introduzca un elemento: ")
    graficoPropio.append(elementos)

print("\nGrafica A")
print("%s\n" %(graficaUno(conversion)))
print("\nGrafica B")
print("%s\n" %(graficaDos(conversion)))
print("\nGrafico C")
print("%s\n" %(graficaTres(conversion) and graficaUno(conversion)))