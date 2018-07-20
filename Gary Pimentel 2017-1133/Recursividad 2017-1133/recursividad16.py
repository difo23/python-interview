def piramide(n,fila = 0):
    filas = 0
    if n == 1:
        return "las filas que se pueden hacer son %d, y las que sobran %d" %(fila,n)
    else:
        filas += 1
        return 1-piramide(n-2,filas + fila)

piramide(46)
  