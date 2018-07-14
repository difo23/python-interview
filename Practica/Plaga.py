print("""Los conejos de Fibonacci. El matemático Leonardo Fibonacci expuso el siguiente problema,
sSuponga que una pareja de conejos tiene un par decriás cada mes 
y a la vez las criás se hacen fértiles al cabo de un mes. Si comenzamos con una pareja fértil y no muere. 
¿Cuantos pares de conejos se tendrían al cabo de un año?""")

parejas = 1
conejos = 0
año = 12 #meses
for i in range(año):
      print("Al %s mes hay %s parejas" %(i+1, parejas))
      conejos, parejas = parejas, conejos+parejas
print("Fin del Programa")