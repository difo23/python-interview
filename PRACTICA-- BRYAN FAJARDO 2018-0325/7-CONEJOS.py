print("la cantidad de parejas de conejos que tendra al cabo de un año es:")
a = 1
b = 0

for i in range(12):
    print("En el mes %d hay %d parejas" % (i+1, a))
    b, a = a, b+a



