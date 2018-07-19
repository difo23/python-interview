def cdig(n, d):    # Este lo envio  usted
    numero = str(n)
    conteo = 0
    digito = str(d)

    for valor in numero:
        if valor == digito:
            conteo +=1

    return conteo


print(cdig(584588, 8))

