def unidadesDeMedida(inches, yardas = 0, pies = 0):
    cantidadYardas = 0
    cantidadPies = 0
    
    if inches >= 36:
        cantidadYardas += 1
        return unidadesDeMedida(inches - 36, yardas + cantidadYardas, pies)

    elif inches >= 12:
        cantidadPies += 1
        return unidadesDeMedida(inches - 12, yardas, pies + cantidadPies)

    else:
        pulgadas = inches
        return "Tienes %d yardas\nTienes %d Pies\nTienes %d pulgadas\n" %(yardas, pies, pulgadas)

pulgadasIntro = int(input("Escriba la cantidad de pulgadas que posea: "))
print(unidadesDeMedida(pulgadasIntro))
         
