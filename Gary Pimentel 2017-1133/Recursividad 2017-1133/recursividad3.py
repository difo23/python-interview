def convertidor(pul, yar = 0, pie = 0):
    yarsuma = 0
    piesuma = 0
    if pul < 12:
        return "pulgada = %d, yarda = %d, pie = %d" %(pul,yar,pie)
    elif pul >= 36:
        yarsuma += 1
        return convertidor(pul-36, yar + yarsuma, pie)
    else:
        piesuma += 1
        return convertidor(pul-12, yar, pie + piesuma) 

print(convertidor(int(input('Cantidad: '))))

