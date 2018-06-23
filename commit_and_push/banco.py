dinero = input("introducir monto a depositar: ")
intereses = input("introducir intereses: ")
tiempo = input("cuantos meses ahorro: ")
meses = tiempo
meses = int(meses)
dinero = int(dinero)
tiempo = int(tiempo)
intereses = int(intereses)
inte1 = intereses * dinero / 100
Tintereses = inte1 * meses
total = Tintereses + dinero
print  (total)
