nom=int(input('ingrese numero de veces que quiera su nombre se repita: '))


def nombre(x):
    if x == 0:
        return
    print('yamile')
    nombre(x-1)

nombre(nom)