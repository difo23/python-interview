# terna es igual a: a^2 + b^2 = c^
# calcular terna con m, n : a= n^2-m^2; b= 2*n*m; c= n^2 + m^2
for contado in range(5):
    n = int(input("Introduce la cantidad n para calcular la terna %d" %(contado+1)))
    m = int(input("Introduce la cantidad m para calcular la terna %d" %(contado+1)))
    if n > m:              # si n > m; a = n^2 - m^2
        a = n**2 - m**2
        b = 2*n * m
        c = n**2 + m**2
    else:                  # si m > n; a= m^2 -n^2
        a = m**2 - n**2
        b = 2*n * m
        c = n**2 + m**2

    print(" Terna Pitagorica %d: es igual a: (%d,%d,%d)" % ((contado+1), a, b, c))