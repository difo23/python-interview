ahorro = input("Digite el monto de ahorro que agregara: ")
ahorro = int(ahorro)
taza = input("Taza de intereses del banco: ")
taza = int(taza)
meses = input("Cantidad de meses que desea calcular: ")
meses = int(taza)
taza = taza/12
taza = taza/100
if ahorro >= 10000:
     dinero = ahorro*taza*meses
     dinero += ahorro
     print("Su nuevo balance en su cuenta %d es de %d" %(cuenta,dinero))
else:
    print("Necesitas 10,000 pesos o mas por regla del banco")