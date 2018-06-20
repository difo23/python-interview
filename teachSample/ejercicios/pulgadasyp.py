# 3.Haga un programa al cual se le digite una longitud expresada en pulgadas e imprima la
# misma longitud en yardas, pies y pulgadas. Por ejemplo una longitud de 65 pulgadas seria
# expresada como 1 yarda, 2 pies y 5 pulgadas.

def longitud(pulgadas):
    yarda = 0 # una yarda tiene 36 pulgadas
    pies = 0 # un pie tiene 12 pulgadas

    while pulgadas >= 36:
        yarda += 1
        pulgadas -= 36

    while pulgadas >= 12:
        pies += 1
        pulgadas -= 12

    print("Las yardas que tienes son: %d" %yarda)
    print("Los pies que tienes son: %d" %pies)
    print("Las pulgadas que te sobran son: %d" %pulgadas)



longitud(65)