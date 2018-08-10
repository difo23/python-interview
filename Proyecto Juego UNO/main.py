import Card
import CurrentScreen
import EnumsCards

print('Bienvenidos al Juego de UNO')
print('Creado por:')
print('Walkely R.  2018-0416| Jhon Luis M.  2018-0307| Bryan F. 2018-0325 ')
print (" ")
# 0: Jugador, 1: KI - Máquina
numberOf = []
startPlayer = 0
numberOf.append(1)
numberOf.append(1)
# dirección 1: en el sentido de las agujas del reloj, -1: en sentido antihorario
pointsOfPlayers = Card.initPointsOfPlayers(numberOf[0] + numberOf[1])
# Tarjetas [1] 0 => + Tarjetas no dibujadas, 1 => dibujadas
drawCards = [0, 0]
#Va a devolver el Valor del Jugador que es (0)
names = Card.getNames(numberOf[0])
names.extend(Card.getKINames(numberOf[1]))
#Suma los puntos de las cartas desechadas
while(Card.someHasEnoughtPoints(pointsOfPlayers) == -1):
    cardStack = Card.initStackOfCards()
    #Cartas Aleatorias
    Card.shuffleDeckofCards(cardStack)
    handsOfCards = []
    for player in range((numberOf[0] + numberOf[1])):
        handsOfCards.append(Card.initHand(cardStack))
    direction = 1
    otherColor = -1
    lastCard = Card.drawCard(cardStack)
    whichPlayer = startPlayer % (numberOf[0]+numberOf[1])
    startPlayer += 1
    if lastCard.getValue() == "roba2":
        if lastCard.backInDeck == 1:
            drawCards[0] = 0
        else:
            drawCards[0] += 2
    elif lastCard.getValue() == "roba4":
        if lastCard.backInDeck == 1:
            drawCards[0] = 0
        else:
            drawCards[0] += 4
        if(lastCard.getColor() == "comodin"):
            if "KI" in names[whichPlayer]:
                colorCardsInHand = [0, 0, 0, 0]
                for card in handsOfCards[whichPlayer]:
                    if(card.color.value <= 4):
                        colorCardsInHand[card.color.value] += 1
                bestColor = colorCardsInHand.index(max(colorCardsInHand))
                otherColor = bestColor
            else:
#Muestra el color elegido en la pantalla, Las cartas en mano, direccion, última Carta y las Cartas Sacadas
                otherColor = CurrentScreen.showChooseColorScreen(
                    "", handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer], drawCards)
    elif lastCard.getValue() == "cambiarColor" and lastCard.getColor() == "comodin":
        if "KI" in names[whichPlayer]:
            colorCardsInHand = [0, 0, 0, 0]
            for card in handsOfCards[whichPlayer]:
                if(card.color.value <= 4):
                    colorCardsInHand[card.color.value] += 1
            bestColor = colorCardsInHand.index(max(colorCardsInHand))
            otherColor = bestColor
        else:
            otherColor = CurrentScreen.showChooseColorScreen(
                "", handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer], drawCards)
    elif lastCard.getValue() == "reverso" and lastCard.backInDeck == 0:
        direction *= -1
        drawCards[1] = 0
    elif lastCard.getValue() == "saltar" and lastCard.backInDeck == 0:
        whichPlayer = (whichPlayer + 1 *
                       direction) % (numberOf[0] + numberOf[1])
        drawCards[1] = 0
    else:
        drawCards[1] = 0
    while Card.someoneWon(handsOfCards) == False:
        if(otherColor != -1):
            #Última carta será igual a la enumeración de carta y color. Del último Valor.
            lastCard = Card.Card(EnumsCards.Colors(otherColor), lastCard.value)
            lastCard.backInDeck = 1
            otherColor = -1
        if "KI" not in handsOfCards[whichPlayer]:
#Mostrará por pantalla (Cartas en mano, última carta, Nombre y las cartas Sacadas).
            CurrentScreen.showCurrentScreen(
                handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer], drawCards)
        lastCardTmp = Card.playCard(handsOfCards[whichPlayer], lastCard, cardStack,
                                    False, names[whichPlayer], direction, drawCards, False)
        if(lastCard.backInDeck == 0):
            cardStack.append(lastCard)
            lastCard.backInDeck = 1
            #Aleatoriza las Cartas Apiladas.
        Card.shuffleDeckofCards(cardStack)
        lastCard = lastCardTmp
        if lastCard.getValue() == "roba2":
            if lastCard.backInDeck == 1:
                drawCards[0] = 0
            else:
                drawCards[0] += 2
        elif lastCard.getValue() == "roba4":
            if lastCard.backInDeck == 1:
                drawCards[0] = 0
            else:
                drawCards[0] += 4
                if(lastCard.getColor() == "comodin"):
                    if "KI" in names[whichPlayer]:
                        colorCardsInHand = [0, 0, 0, 0]
                        for card in handsOfCards[whichPlayer]:
                            if(card.color.value <= 4):
                                colorCardsInHand[card.color.value] += 1
                            bestColor = colorCardsInHand.index(
                                max(colorCardsInHand))
                            otherColor = bestColor
                    else:
                        otherColor = CurrentScreen.showChooseColorScreen(
                            "", handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer], drawCards)
        elif lastCard.getValue() == "cambiarColor" and lastCard.getColor() == "comodin":
            if "KI" in names[whichPlayer]:
                colorCardsInHand = [0, 0, 0, 0]
                for card in handsOfCards[whichPlayer]:
                    if(card.color.value <= 4):
                        colorCardsInHand[card.color.value] += 1
                    bestColor = colorCardsInHand.index(max(colorCardsInHand))
                    otherColor = bestColor
            else:
                otherColor = CurrentScreen.showChooseColorScreen(
                    "", handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer], drawCards)
        elif lastCard.getValue() == "reverso" and lastCard.backInDeck == 0:
            direction *= -1
            drawCards[1] = 0
        elif lastCard.getValue() == "saltar" and lastCard.backInDeck == 0:
            whichPlayer = (whichPlayer + 1 *
                           direction) % (numberOf[0] + numberOf[1])
            drawCards[1] = 0
        else:
            drawCards[1] = 0
        whichPlayer = (whichPlayer + 1 *
                       direction) % (numberOf[0] + numberOf[1])
    winningPerson = (whichPlayer + 1 * direction * -
                     1) % (numberOf[0] + numberOf[1])
    print("¡Enhorabuena a " +
          names[winningPerson] + " por ganar esta ronda!")
    Card.givePersonPoints(handsOfCards, winningPerson, pointsOfPlayers)
    CurrentScreen.showPointsOfPlayers(pointsOfPlayers, names)
    input("Presione OK para continuar")

print("¡Enhorabuena a " + names[(whichPlayer - 1 * direction * -1) %
                                    (numberOf[0] + numberOf[1])] + " Por ganar el Juego")
