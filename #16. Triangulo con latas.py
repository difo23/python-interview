def latas(l):

    niveles = 0
    cantidadLatas = l

    for i in range(0, cantidadLatas, 2):

        if cantidadLatas >= i+1:
            niveles += 1
            cantidadLatas -= i+1

    print("Con %d latas de leche condensada, se hace %d niveles \nsobran %d latas" % (l, niveles, cantidadLatas))


latas(13)
latas(50)
latas(84)
latas(3896)
