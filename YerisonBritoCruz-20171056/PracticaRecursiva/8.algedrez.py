def cuadricula(grano):

    if grano == 0 or grano == 1:

        return 1
    else:
        return 2**grano-1


print("Un total de %d granos de trigos" % (cuadricula(64)))
