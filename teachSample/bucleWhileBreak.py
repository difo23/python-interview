SECRETO = "Secreto"
intentos = 0
password = ""

while intentos < 3:
    
    password = input("introduce el password:")
 
    if password == SECRETO:
      break
    intentos +=1
    print("Intentos %d veulve a tratar . \n" %intentos)

print("Intentos fallidos %d ."%intentos)


    
