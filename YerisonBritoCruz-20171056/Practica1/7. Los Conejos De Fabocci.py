print("Los conejos de Fibonacci. El matemático Leonardo Fibonacci expuso el siguiente problema,"
      "\nSuponga que una pareja de conejos tiene un par de criás cada mes y a la vez las criás"
      "\nse hacen fértiles al cabo de un mes. Si comenzamos con"
      "\nuna pareja fértil y no muere. ¿Cúantos pares de conejos se tendrían al cabo de un año?  ")
parejas = 1
conejo = 0

for i in range(12):
    print("En el mes %d hay %d parejas" % (i+1, parejas))
    conejo, parejas = parejas, conejo+parejas




