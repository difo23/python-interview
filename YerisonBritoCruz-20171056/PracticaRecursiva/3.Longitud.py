
def longitud(pulgadas, yardas=0, pie=0):

    contYarda = 0
    contPie = 0

    if pulgadas < 12:
        return "%d yardas \n%d pie \n%d pulgadas" % (yardas, pie, pulgadas)

    elif pulgadas >= 36:
        contYarda += 1
        return longitud(pulgadas - 36, yardas + contYarda, pie)
    else:
        contPie += 1
        return longitud(pulgadas - 12, yardas, pie + contPie)


entrada = int(input("Introduce la longitud en pulgadas"))

print(longitud(entrada))

