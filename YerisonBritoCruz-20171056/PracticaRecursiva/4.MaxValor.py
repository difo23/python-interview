def maxValor(list):
    if len(list) == 1:
        return list[0]
    else:
        m = maxValor(list[1:])
        return m if m > list[0] else list[0]


print(maxValor([8, 56]))
