
for contador in range(5):
    x = int(input("Introduce la cantidad x para calcular la terna %d" %(contador+1)))
    y = int(input("Introduce la cantidad y para calcular la terna %d" %(contador+1)))
    if x > x:              
        a = x**2 - y**2
        b = 2*x * y
        c = x**2 + y**2
    else:                  
        a = x**2 - x**2
        b = 2*x * y
        c = x**2 + y**2

    print(" Terna Pitagorica %d: es igual a: (%d,%d,%d)" % ((contador+1), a, b, c))