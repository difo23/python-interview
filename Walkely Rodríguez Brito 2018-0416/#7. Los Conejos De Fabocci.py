print("Los conejos de Fibonacci. ¿Cúantos pares de conejos se tendrían al cabo de un año?  ")
parejas = 1
conejo = 0

for i in range(12):
    print("En el mes %d hay %d parejas" % (i+1, parejas))
    conejo, parejas = parejas, conejo+parejas




