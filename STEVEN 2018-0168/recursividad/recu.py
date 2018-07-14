nom = input("escribe tu nombre: ")
veces = int(input("cuantas veces quiere repetirlo: "))
def nombre(n):
    if n ==0:
        return("fin")
    print(nom)
    nombre(n-1)

print(nombre(veces)) 
# como se quitara esa wea de none O.o      