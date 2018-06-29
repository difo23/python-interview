pulgada = int(input("Favor de introducir un número de longitud en pulgada:"))
yardas = 0
pie = 0

print(" %d pulgadas se expresa como: " % pulgada)

for p in range(pulgada, 35, -36):           
      pulgada -= 36
      yardas += 1

for y in range(pulgada, 11, -12):               
      pulgada -= 12
      pie += 1

print(" %d yardas \n %d pies \n %d pulgadas" % (yardas, pie, pulgada))
