'''Comentarios de varias lineas diferentes de # que es una sola linea.
Este programa se repetira 3 veces o hasta que se ingrese la palabra "secreto" y desplegara el numero de intentos hasta que
cualquiera de los eventos ocurra.
'''
password= "secreto"
entrada =''
suma= 0
while suma < 3 and entrada != password :
    # introduce en terminal la clave usando "" o te dara error!
    entrada = input("Introduce la palabra secreta: ")
    suma += 1
    print("Intento %d.\n" %suma)
    #print("Intento "+str(suma))
print("Utilizaste %d intentos." %suma)

