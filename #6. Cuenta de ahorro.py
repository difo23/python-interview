libreta = int(input("Introduce la cantidad que deceas ahorrar "
                    "\nPara obtener ganacias necesitas tener mas de 4000 $RD ahorrados"))

tasa = int(input("Introduce la tasa de intereses anuales \nTasa común de 5% a 20% anuales"))
meses = int(input("¿Cúantos meses quieres consultar?"))
tasa = tasa/12    # el usuario introduce la tasa anual

if libreta >= 4000:
    ganacias = libreta*(tasa/100)*meses
    total = ganacias + libreta
    print("En %d meses usted tendra una ganancia de %d $Rd \nSu capital será de %d $Rd" % (meses, ganacias, total))
else:
    print("Tienes ahorrado %d "
          " Necesitas ahorrar mas de 4000 $RD para obtener ganacias" % libreta)
