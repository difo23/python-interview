for contador in range(5):
    primernum = int(input("Introduce la %d cantidad: " %(contador+1)))
    segundonum = int(input("Introduce la %d cantidad: " %(contador+1)))
    if primernum > segundonum:              
        a = primernum**2 - segundonum**2
        b = 2*primernum * segundonum
        c = primernum**2 + segundonum**2
        print("Utilizando metodo normal")
        print("La terna Pitagorica de %d es igual a: %d,%d y %d" %((contador+1), a, b, c))
    else:   
        a = segundonum**2 - primernum**2
        b = 2*primernum * segundonum
        c = primernum**2 + segundonum**2
        print("Aplicado ley conmutitativa")     
        print("La terna Pitagorica de %d es igual a: %d,%d y %d" %((contador+1), a, b, c))