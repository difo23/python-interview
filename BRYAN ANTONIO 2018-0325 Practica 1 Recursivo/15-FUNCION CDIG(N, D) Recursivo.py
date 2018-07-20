def cdig(n, d):
    repeticiones = 0
    if n == 0:
        return repeticiones
    elif n % 10 == d:
        return repeticiones+1 + cdig(n//10, d)

    else:
        return cdig(n//10, d)


print(cdig(584588, 8))
