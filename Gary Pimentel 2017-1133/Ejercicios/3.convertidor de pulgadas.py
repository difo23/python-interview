print("bienvenidos al convertidor de pulgada a pies y yarda")
convertidor = input("introduzca la medida ") 
convertidor = int(convertidor)
yar = 0
pie = 0
while convertidor > 36:
    convertidor -= 36
    yar += 1
while convertidor > 12:
    convertidor -= 12
    pie += 1
print("medida en yarda %d" %yar)
print("medida en pies %d" %pie)
print(convertidor)