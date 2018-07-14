ahorrar = float(input("Digite la cantidad a ahorrar pls: "))
meses = int(input("Digite la cantidad de meses pls: "))
interes = float(input("Digite la interes de meses pls: "))
interes=interes/100
monto = ahorrar
i=0
while i<meses:
    monto = monto+(monto * interes)
    i=i+1

print("El total es igual: " + str(monto))