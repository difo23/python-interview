a = float(input("Ingrese un numero:"));
contador = int(1);
division = float(0);

if a <= 0:
  while a <= 0:
    print("Error, Ingrese un numero positivo diferente de 0");
    a = float(input("Ingrese otro numero:"));

while(a > contador):
  division = a/contador;
  if division % 1 == 0:
    print(division); 
  contador += 1;
