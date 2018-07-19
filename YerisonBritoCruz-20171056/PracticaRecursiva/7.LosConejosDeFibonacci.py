def conejo(meses):
    if meses == 0:
        return 0
    elif meses == 1:
        return 1
    else:
        return conejo(meses-1) + conejo(meses-2)

print(conejo(12))
print(conejo(10))


