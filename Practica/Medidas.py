yardas = 0
pies = 0 
pulgadas = 0

print("vamos a convertir pulgadas, en yardas, pies y pulgadas")
pulgadas_introducidas = int(input("Introduzca la cantidad de pulgadas: "))

while pulgadas_introducidas >= 36:
    yardas+= 1
    pulgadas_introducidas -= 36

while pulgadas_introducidas >= 12:
    pies+= 1
    pulgadas_introducidas -= 12

pulgadas = pulgadas_introducidas

print("Usted tiene:\n%s yardas\n%s pies\n%s pulgadas" %(yardas, pies, pulgadas))
print("Fin del Programa")