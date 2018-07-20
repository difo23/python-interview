def conejos(cantidad):
    if cantidad == 0:
        return 0
    elif cantidad == 1:
        return 1
    else:
        return conejos(cantidad-1) + conejos(cantidad-2)

print(conejos(12))
print(conejos(10))
