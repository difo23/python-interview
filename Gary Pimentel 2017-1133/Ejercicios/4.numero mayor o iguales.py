print("Bienvenidos")
print("De la funcion maxVal(n, m)")
print("n sera el primero numero y m el segundo")
x = input("Escriba el primer numero ")
x = int(x)
y = input("escriba el segundo numero ")
y = int(y)
if x > y:
    print("el numero n = %d es mayor que m = %d") %(x,y)
elif x == y:
        print("el numero n = %d es igual que m = %d") %(x,y)   
else:
    print("el numero n = %d es menor que m = %d") %(x,y)
