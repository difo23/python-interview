monto = float(input("ingrese el monto a ahorrar:"));
interes = float(input("ingrese la tasa de interes:"));
meses = float(input("ingrese los meses de ahorro:"));
contador = float(1);
b = int(1);

print("");
while(meses > contador):
  print("meses",b,":$",(monto*interes)*contador);
  b += 1;
  contador += 1;

print("");
print("el monto final del ahorro es:$",(monto*interes)*meses);
