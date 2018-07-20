def cuentaAhorro(ahorro):
 numero = 0
 numero2 = int(1);

 if(numero > contador):
   print("meses",b,":$",(monto*interes)*contador);
   numero2 += 1;
   contador += 1;
   ahorro = ahorro * cuentaAhorro(ahorro-1)
 return

monto = float(input("ingrese el monto a ahorrar:"));
interes = float(input("ingrese la tasa de interes:"));
meses = float(input("ingrese los meses de ahorro:"));
contador = float(1);

print("");
print("el monto final del ahorro es:$",(monto*interes)*meses);
