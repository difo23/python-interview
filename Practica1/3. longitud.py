pulgada = int(input("Introduce la longitud en pulgada:"))
yardas = 0
pie = 0

print(" %d pulgadas se expresa como: " % pulgada)

for i in range(pulgada, 35, -36):                 # 1 yardas = 36 p
    pulgada -= 36
    yardas += 1

for j in range(pulgada, 11, -12):                 # 1 pie = 12 p
        pulgada -= 12
        pie += 1

print(" %d yardas \n %d pies \n %d pulgadas" % (yardas, pie, pulgada))
