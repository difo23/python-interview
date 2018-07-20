def ajedrez(piezas):

    if piezas == 0 or piezas == 1:

        return 1
    else:
        return 2**piezas-1


print("%d granos de trigos" % (ajedrez(64)))
print("Terminado")
