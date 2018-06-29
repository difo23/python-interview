def latas(l):

    niveles = 0
    cantidad = l

    for i in range(0, cantidad, 2):

        if cantidad >= i+1:
            niveles += 1
            cantidad-= i+1

    print("Con %d  de latas , se hace %d niveles \nsobran %d latas" % (l, niveles, cantidad))


latas(13)
latas(18)
latas(260)
latas(5987)