numero = int(input("numero: "))
for i in range(1,numero):
     if numero % i == 0:
        print(i)
if numero < 0:
          print("solo numeros positivos")
if numero == 0:
          print("cero no se puede dividir :v")