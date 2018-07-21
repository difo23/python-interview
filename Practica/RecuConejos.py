print ("""El matemático Leonardo Fibonacci expuso el siguiente problema,
haga un programa para solucionarlo. Suponga que una pareja de conejos tiene un par de
criás cada mes y a la vez las criás se hacen fértiles al cabo de un mes. Si comenzamos con
una pareja fértil y no muere. ¿Cuantos pares de conejos se tendrían al cabo de x meses?""")

def paresConejos(meses):
    if meses == 0:
        return 0
    elif meses == 1:
        return 1
    else:
        return paresConejos(meses-1) + paresConejos(meses-2)

meses = int(input("Por cuantos meses crian?\n"))
parejas = (paresConejos(meses) // 2)
print("Usted tiene %d conejos y %d parejas" %(paresConejos(meses), parejas))