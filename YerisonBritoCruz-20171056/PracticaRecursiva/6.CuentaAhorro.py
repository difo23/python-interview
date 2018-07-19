def cuenta(ahorro, tasa, meses, ganancia=0):
    tasa = tasa/12
    if ganancia > 0:

        return "En %d meses usted tendra una ganancia de %d $Rd \nSu capital será de %d $Rd"\
               % (meses, ganancia, ahorro+ganancia)
    else:
        return cuenta(ahorro, tasa, meses, ganancia+(ahorro*(tasa/100)*meses))


print(cuenta(500, 10, 12))
