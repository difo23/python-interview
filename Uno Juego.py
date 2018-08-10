from random import shuffle
#Los numeros representan el numero de carta, las cartas especiales son 10,11,12,13,14
#La carta 10=comodin
#La carta 11=paso
#La carta 12=roba2
#La carta 13=cambio de color
#La carta 14=roba cuatro y cambia color

cartas = {'rojo':[0,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
          'amarillo':[0,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
          'verde':[0,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
          'azul':[0,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,13,14]}

puntos_x_jugador = {0:0,1:0}
jugador0= {'rojo':[],'amarillo':[],'verde':[],'azul':[]}
jugador1= {'rojo':[],'amarillo':[],'verde':[],'azul':[]}
jugador =  [jugador0, jugador1]
colores=['rojo','amarillo','verde','azul']
jugadas = []
posibles_jugadas = {'rojo':[],'amarillo':[],'verde':[],'azul':[]}
turno=[0,1,0]
ultimo_color=''
ultimo_numero=''


def repartir(cartas, jugador, turno):
    for y in range(0,7):
        shuffle(colores)
        shuffle(cartas[colores[0]])
        jugador[0][colores[0]].append(cartas[colores[0]][len(cartas[colores[0]])-1])
        cartas[colores[0]].pop(len(cartas[colores[0]])-1)

    for y in range(0,7):
        shuffle(colores)
        shuffle(cartas[colores[0]])
        jugador[1][colores[0]].append(cartas[colores[0]][len(cartas[colores[0]])-1])
        cartas[colores[0]].pop(len(cartas[colores[0]])-1)

def primera_carta(cartas, jugadas, colores):
    shuffle(colores)
    shuffle(cartas[colores[0]])
    ultimo_col=colores[0]
    ultimo_num=cartas[colores[0]][len(cartas[colores[0]])-1]
    if ultimo_num == 10 or ultimo_num == 11 or ultimo_num == 12 or ultimo_num == 13 or ultimo_num == 14:
        primera_carta(cartas, jugadas, colores)
    else:
        jugadas.append(ultimo_col)
        jugadas.append(ultimo_num)
        cartas[colores[0]].pop(len(cartas[colores[0]])-1)
    return ultimo_col, ultimo_num

def primer_turno(turno):
    shuffle(turno)

def cambia_turno(turno):
    tur=turno[0]
    turno[0]=turno[1]
    turno[1]=tur

def fin_por_carta(cartas):
    for clave in cartas:
        if len(cartas[clave])>0:
            return False
    return True

def puntos_restantes(jugador,turno):
    for clave in jugador[turno[1]]:
        for valor in jugador[turno[1]][clave]:
            if (valor >=0 and valor<=9):        
                puntos_x_jugador[turno[0]]+=valor
            elif (valor >=10 and valor<=12):
                puntos_x_jugador[turno[0]]+=20
            else:
                puntos_x_jugador[turno[0]]+=50
                
def fin_por_puntaje(cartas, turno):
    if(puntos_x_jugador[turno[0]]>=500):
        puntos_restantes(jugador,turno)
        return False
    return True

def reinicio_jugada(cartas, jugador, turno):
    cartas = {'rojo':[0,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
          'amarillo':[0,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
          'verde':[0,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
          'azul':[0,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,13,14]}
    repartir(cartas, jugador, turno)
                

def nueva_carta(cartas, jugador, turno):
    if (fin_por_carta(cartas)):
        print ('No quedan cartas para repartir')
        if(fin_por_puntaje(cartas, turno)):
            print('Fin del juego')
            if turno[0]==0:
                print('Ganador: Machine')
            else:
                print('Ganador: Jugador')
        else:
            reinicio_jugada(cartas, jugador, turno)
            cambia_turno(turno)
            nueva_carta(cartas, jugador, turno)
        if (valid_posible_jugada(jugador, jugadas, turno)):
            return False
        else:
            return True
    else:
        shuffle(colores)
        if len(cartas[colores[0]])>0: 
            shuffle(cartas[colores[0]])
            jugador[turno[0]][colores[0]].append(cartas[colores[0]][len(cartas[colores[0]])-1])
            cartas[colores[0]].pop(len(cartas[colores[0]])-1)
        else:
            nueva_carta(cartas, jugador, turno)
        return True

            
def carta_multa(valor):
    if valor == 10:
        return True
    if valor == 12:
        return True
    if valor == 13:
        return True
    if valor == 14:
        return True
    return False


def multas(turno, color, valor, jugador, jugadas, cartas):
    if valor == 10:
        puntos_x_jugador[turno[0]]+=20
    if valor == 11:
        puntos_x_jugador[turno[0]]+=20
    if valor == 12:
        puntos_x_jugador[turno[0]]+=20
        cambia_turno(turno)
        nueva_carta(cartas, jugador, turno)
        nueva_carta(cartas, jugador, turno)
        cambia_turno(turno)
    if valor == 13:
        color=''
        puntos_x_jugador[turno[0]]+=50
        op=0
        if turno[0]==0:
            op=1
        else:
            op=int(input('Digite el color(1=Rojo, 2=Amarillo, 3=Verde, 4=Azul):'))
        if op==1:
            color='rojo'
        if op==2:
            color='amarillo'
        if op==3:
            color='verde'
        if op==4:
            color='azul'
        jugadas.append(color)
        jugadas.append(valor)
    if valor == 14:
        puntos_x_jugador[turno[0]]+=50
        cambia_turno(turno)
        nueva_carta(cartas, jugador, turno)
        nueva_carta(cartas, jugador, turno)
        nueva_carta(cartas, jugador, turno)
        nueva_carta(cartas, jugador, turno)
        cambia_turno(turno)
        color=''
        op=0
        if turno[0]==0:
            op=1
        else:
            op=int(input('Digite el color(1=Rojo, 2=Amarillo, 3=Verde, 4=Azul):'))
        if op==1:
            color='rojo'
        if op==2:
            color='amarillo'
        if op==3:
            color='verde'
        if op==4:
            color='azul'
        jugadas.append(color)
        jugadas.append(valor)

def valid_posible_jugada(jugador, jugadas, turno):
    var = False
    if len(jugador[turno[0]][jugadas[len(jugadas)-2]])>0:
        for valor in jugador[turno[0]][jugadas[len(jugadas)-2]]:
            var=True
    for clave in jugador[turno[0]]:
        if jugadas[len(jugadas)-2]!= clave:
            if jugadas[len(jugadas)-1] in jugador[turno[0]][clave]:
                var=True
            if 13 in jugador[turno[0]][clave]:
                var=True
            if 14 in jugador[turno[0]][clave]:
                var=True
    return var

def posible_jugada(jugador, jugadas, turno):
    var = False
    if len(jugador[turno[0]][jugadas[len(jugadas)-2]])>0:
        for valor in jugador[turno[0]][jugadas[len(jugadas)-2]]:
            print(jugadas[len(jugadas)-2]+'->'+str(valor))
            if turno[0]==0:
                posibles_jugadas[jugadas[len(jugadas)-2]].append(valor)               
            var=True
    for clave in jugador[turno[0]]:
        if jugadas[len(jugadas)-2]!= clave:
            if jugadas[len(jugadas)-1] in jugador[turno[0]][clave]:
                if turno[0]==0:
                    posibles_jugadas[clave].append(jugadas[len(jugadas)-1])
                print(clave+'->'+str(jugadas[len(jugadas)-1]))
                var=True
            if 13 in jugador[turno[0]][clave]:
                if turno[0]==0:
                    posibles_jugadas[clave].append(13)
                print(clave+'->'+str(13))
                var=True
            if 14 in jugador[turno[0]][clave]:
                if turno[0]==0:
                    posibles_jugadas[clave].append(14)
                print(clave+'->'+str(14))
                var=True
    return var


def sacar_carta_jugador(jugador, turno, color, valor, jugadas, cartas):
    if(valid_posible_jugada(jugador, jugadas, turno)):
        if valor in jugador[turno[0]][color]:
            jugadas.append(color)
            jugadas.append(valor)
            jugador[turno[0]][color].remove(valor)
            if(carta_multa(valor)):
                multas(turno, color, valor, jugador, jugadas, cartas)
                sacar_carta_jugador(jugador, turno, color, valor, jugadas, cartas)
            else:
                puntos_x_jugador[turno[0]]+=valor
            return True
    else:
        nueva_carta(cartas, jugador, turno)
        sacar_carta_jugador(jugador, turno, color, valor, jugadas, cartas)
    return False

def buscar_lista(posibles_jugadas, color, numero):
    try:
        if numero in posibles_jugadas[color]:
                return True
    except:
        buscar_lista(posibles_jugadas, color, numero)
    return False


def is_not_null(posibles_jugadas):
    for clave in posibles_jugadas:
        if len(posibles_jugadas[clave])>0:
            return True
    return False

def elegir_jugada(cartas, jugador, turno, jugadas):
    if (fin_por_puntaje(cartas, turno)):
        print('Ultima jugada, Color:'+jugadas[len(jugadas)-2]+', Carta:'+str(jugadas[len(jugadas)-1]))
        if turno[0]==0:
            print('Turno de Machine, Puntaje:('+str(puntos_x_jugador[0])+')')
            print('Cartas',jugador[turno[0]])
        if turno[0]==1:
            print('Turno de Jugador, Puntaje:('+str(puntos_x_jugador[1])+')')
            print('Cartas',jugador[turno[0]])
        if(valid_posible_jugada(jugador, jugadas, turno)):
            posible_jugada(jugador, jugadas, turno)
            color=''
            numero=''
            if turno[0]==0:
                for clave in posibles_jugadas:
                    if len(posibles_jugadas[clave])>0:
                        shuffle(posibles_jugadas[clave])
                        color=clave
                        numero=posibles_jugadas[clave][0]
            if turno[0]==1:
                color = str(input('Digite el color de su jugada:'))
                numero = int(input('Digite el numero a jugar:'))
            if(sacar_carta_jugador(jugador, turno, color, numero, jugadas, cartas)):
               cambia_turno(turno)
               elegir_jugada(cartas, jugador, turno, jugadas)
            else:
                if (nueva_carta(cartas, jugador, turno)):
                    elegir_jugada(cartas, jugador, turno, jugadas)
        else:
            if(nueva_carta(cartas, jugador, turno)):
                elegir_jugada(cartas, jugador, turno, jugadas)
        return False
    else:
        if turno[0]==0:
            print('Turno de Machine, Puntaje:('+str(puntos_x_jugador[0])+')')
        if turno[0]==1:
            print('Turno de Jugador, Puntaje:('+str(puntos_x_jugador[1])+')')
        print('El jugador Ha Ganado')
        

def jugar(cartas, jugador, ultimo_col, ultimo_num, posibles_jugadas, turno):
    if(buscar_lista(posibles_jugadas, color, numero)):
            ultimo_col, ultimo_num = str(color), int(numero)
            cambia_turno(turno)
            multas(turno, color, numero, jugador, cartas)
            elegir_jugada(cartas, jugador[turno[0]], ultimo_col, ultimo_num, posibles_jugadas, turno)
    else:
        print('\nJugada no Valida\n')
        elegir_jugada(cartas, jugador[turno[0]], ultimo_col, ultimo_num, posibles_jugadas, turno)
        if turno[2]<1:
            turno[2]=turno[2]+1
            print('\nNo tenia jugadas, se le dio nueva carta\n')
            nueva_carta(cartas,jugador,turno)
            posible_jugada(jugador, colores, ultimo_col, ultimo_num, pos_jugadas, turno)
            elegir_jugada(cartas, jugador[turno[0]], ultimo_col, ultimo_num, posibles_jugadas, turno, colores)
        else:
            cambia_turno(turno)
            turno[2]=0
            elegir_jugada(cartas, jugador[turno[0]], ultimo_col, ultimo_num, posibles_jugadas, turno, colores)



repartir(cartas, jugador, turno)
primera_carta(cartas, jugadas, colores)
primer_turno(turno)

while(fin_por_carta(cartas)!=True):
    elegir_jugada(cartas, jugador, turno, jugadas)
