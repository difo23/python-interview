def triangulo(niveles):

    if niveles <= 1:
        return niveles
    else:
        return triangulo(niveles - 1) + 2


def niveles(latas, contador=0):

    if latas < triangulo(contador):
        return "%d Nieveles y sobran %d latas" % (contador, latas)

    else:
        return niveles(latas-triangulo(contador+1), contador+1)


print(niveles(13))
print(niveles(3896))
print(niveles(84))
print(niveles(16))
