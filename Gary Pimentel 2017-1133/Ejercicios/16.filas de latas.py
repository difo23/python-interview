def piramide(n):
    pisos = 0
    filasdelatas = n
    for x in range(0, filasdelatas, 2):
        if filasdelatas >= x+1:
            pisos += 1
            filasdelatas -= x+1

    print("Si piensa hacer una fila de latas con esta cantidad '%d' se puede obtener:" %n) 
    print("Estas son las filas o pisos que puede hacer: %d" %pisos)
    print("Estas son las latas que sobran: %d" %filasdelatas)

piramide(46)