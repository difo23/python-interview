l = []
v = 0
s = 0
c = 0
p = 0
numer = int(input("Ecribe un numero: "))    

for cont in range(0, numer):
    p += 1
    v = int(input("Escribe el valor %d :" % (cont+1)))
    l.append(v)
    s = s+l[cont]
    c = c+(l[cont]**2)

promedio = s/p

print("La suma de los %d valores es igual a: %d \nLa suma de los cuadrado es igual: %d " % (v, s, c))
print("El Valor maximo introducido es igual a %d \nEl valor minimo introducido es igual a: %d"
      "\nEl promedio es igual a: %d" % (max(l), min(l), p))
