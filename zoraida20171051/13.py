for terna in range(5):
    a = int(input("Introduce la cantidad a para calcular la terna %d : " %(terna+1)))
    b = int(input("Introduce la cantidad b para calcular la terna %d : " %(terna+1)))
    if a > b:           
        c = a**2 - b**2
        d = 2*a * b
        e = a**2 + b**2
    else:                 
        c = a**2 - b**2
        d = 2*a * b
        e = a**2 + b**2

    print("  Pitagorica %d: es igual a: (%d,%d,%d)" % ((terna+1), c, d, e))