#Escribir un programa al cual se digite un numero e imprima por pantalla su nombre tantas veces como lo indique el numero digitado
a = int(input("Introduce un numero: "))

if a == 0:
	b="cero"
if a == 1:
	b="uno"
if a == 2:
	b="dos"
if a == 3:
	b="tres"
if a == 4:
	b="cuatro"
if a == 5:
	b="cinco"
if a == 6:
	b="seis"
if a == 7:
	b="siete"
if a == 8:
	b="ocho"
if a == 9:
	b="nueve"
if a == 10:
	b="diez"

i=0
while i < a:
    print(b)
    i=i+1
print("Press enter to continue")