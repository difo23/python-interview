print("la cantidad de parejas de conejos que tendra al cabo de un ano es:")
pareja = 1
conejo = 0

for i in range(12):
    print("En el mes %d hay %d parejas" % (i+1, pareja))
    conejo, pareja = pareja, conejo+pareja



