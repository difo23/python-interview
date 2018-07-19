def gauss(number):
    if number == 1:
        return 1
    else:
        return number + gauss(number - 1)


print(gauss(5))

print(gauss(100))

print(gauss(991))