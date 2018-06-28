a = float(input("Introduce un numero: "))
b = a%1
a = int(a)
yardas = int(a/36)
a = a%36
pies = int((a)/12)
a = a%12
pulgadas = (float(a))+b
print("Yardas = "+ str(yardas))
print("Pies = "+ str(pies))
print("Pulgadas = "+ str(pulgadas))

