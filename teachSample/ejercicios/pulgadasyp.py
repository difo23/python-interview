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


def cantidad(pesos):
    cientos = 0 # una yarda tiene 36 pulgadas
    cincuenta = 0 # un pie tiene 12 pulgadas
    veinte= 0
    cinco= 0
    print("Introduciste %d pesos y te devolvemos:" %pesos)
    while pesos >= 100:
        cientos  += 1
        pesos -= 100

    while pesos >= 50:
        cincuenta  += 1
        pesos -= 50

    while pesos >= 20:
        veinte += 1
        pesos -= 20

    while pesos >= 5:
        cinco += 1
        pesos -= 5
    
    print(" %d Billetes de 100, %d billetes de 50, %d billetes de 20, %d billetes de 5 y %d pesos " %(cientos, cincuenta, veinte, cinco, pesos))



def cantidad2(pesos):
    cientos = 0 # una yarda tiene 36 pulgadas
    cincuenta = 0 # un pie tiene 12 pulgadas
    veinte= 0
    cinco= 0
    print("Introduciste %d pesos y te devolvemos:" %pesos)
    if pesos >= 100:
        cientos = pesos//100
        pesos -= cientos*100

    if  pesos >= 50:
        cincuenta = pesos//50
        pesos -= cincuenta*50

    if pesos >= 20:
        veinte = pesos//20
        pesos -= veinte*20

    if pesos >= 5:
        cinco =pesos//5
        pesos -= cinco*5
    
    print(" %d Billetes de 100, %d billetes de 50, %d billetes de 20, %d billetes de 5 y %d pesos " %(cientos, cincuenta, veinte, cinco, pesos))


cantidad2(13577)
#longitud(65)