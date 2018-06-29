def latas(l):

    niveles = 0
    cantiadLatas = l

    for i in range(0, cantiadLatas, 2):

        if cantiadLatas >= i+1:
            niveles += 1
            cantiadLatas -= i+1

    print("Con %d latas de leche condensada, se hace %d niveles \nsobran %d latas" % (l, niveles, cantiadLatas))


latas(13)
latas(50)
latas(84)
latas(3896)
