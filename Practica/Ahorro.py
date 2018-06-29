libreta_ahorro = int(input("Escribe la cantidad que quieres ahorrar\nEl banco BHD permite un monto minimo de 2500$RD")

intereses = 10
print("Nuestro interes es de un 10%")
interes = intereses/12
meses = int(input("Cuantos meses vas a consultar?))

if libreta_ahorro >= 2500:
    ganancia = (interes/100)*meses*libreta_ahorro
    total = ganancia+libreta_ahorro\
    print("En %s meses tendra una ganancia de %s pesos para un total de: %s$RD" %(meses, ganancia, total))
print("Fin del Programa")