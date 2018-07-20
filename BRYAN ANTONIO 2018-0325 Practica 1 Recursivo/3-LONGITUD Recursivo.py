def longitud (pulgadas):
 numero = 0

 if (numero >= 1):

    if pulgadas == 1:
        pulgadas +=1

    if numero < pulgadas:
        pulgadas = pulgadas * longitud(pulgadas-1)
    return;

pulgadas = float(input("ingrese una longitud"));
yardas = float(pulgadas*0.0277778);
pies = float(pulgadas*0.0833333);

print("");
print("pulgadas:  ", pulgadas);
print("yardas:", yardas);
print("pies:", pies);

