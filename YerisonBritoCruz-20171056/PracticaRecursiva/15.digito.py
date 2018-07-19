def cdig(n, d):
    conteo = 0
    if n == 0:
        return conteo
    elif n % 10 == d:
        return conteo+1 + cdig(n//10, d)

    else:
        return cdig(n//10, d)


print(cdig(584588, 8))
print(cdig(1241, 1))
