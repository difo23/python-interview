import random
import CurrentScreen
from EnumsCards import *
CONST_START_NUMBER_OF_HANDS = 7


class Card():

    def __init__(self, color, value):
        self.color = color
        self.value = value
        self.backInDeck = 0

    def getColor(self):
        return self.color.name

    def getValue(self):
        return self.value.name

    def setColor(self, color):
        self.color = color


def createColorStack(color):
    colorStack = []

    if(color.value < 4):
        for value in Values:
            if(value.value == 0):
                colorStack.append(Card(color, value))
            elif value.value > 13:
                pass
            else:
                colorStack.append(Card(color, value))
                colorStack.append(Card(color, value))
    else:
        for value in Values:
            if value.value > 13:
                colorStack.append(Card(color, value))
                colorStack.append(Card(color, value))

    return colorStack


def initStackOfCards():
    cardStack = []
    for color in Colors:
        cardStack.extend(createColorStack(color))
    return cardStack


def shuffleDeckofCards(stack):
    for i in range(1000):
        r1 = random.randrange(len(stack))
        r2 = random.randrange(len(stack))
        stack[r1], stack[r2] = stack[r2], stack[r1]


def drawCard(stack):
    try:
        nextCard = stack.pop(0)
        nextCard.backInDeck = 0
        return(nextCard)
    except:
        print("¡Demasiado Jugadores!")
        exit(0)


def initHand(stack):
    hand = []
    for card in range(CONST_START_NUMBER_OF_HANDS):
        hand.append(stack.pop(0))
    return sortHand(hand)


def someoneWon(handsOfCards):
    for hand in handsOfCards:
        if len(hand) == 0:
            return True
    return False


def sameColor(card, lastCard):
    if card.getColor() == lastCard.getColor():
        return True
    return False


def sameValue(card, lastCard):
    if card.getValue() == lastCard.getValue():
        return True
    return False


def canBeThrown(card, lastCard):
    if(sameColor(card, lastCard) or sameValue(card, lastCard)or card.getColor() == "comodin"):
        return True
    return False


def playCard(hand, lastCard, cardStack, hasDrawnCard, playerName, direction, drawCards, saidUNO):
    if "KI" in playerName:
        return playCardKI(hand, lastCard, cardStack, hasDrawnCard, playerName, direction, drawCards, saidUNO)
    else:
        whichCard = input("Cual Carta va a Jugar: ")
        if whichCard == "d" or whichCard == "D":
            if drawCards[0] > 0:
                for card in range(drawCards[0]):
                    hand.append(drawCard(cardStack))
                drawCards[1] = 1
                sortHand(hand)
                return lastCard
            elif hasDrawnCard == False:
                hand.append(drawCard(cardStack))
                sortHand(hand)
                hasDrawnCard = True
                CurrentScreen.showCurrentScreen(
                    hand, direction, lastCard, playerName, drawCards)
            else:
                print("Ya usted ha tomado '1' Carta, Pase el Turno.")
            return playCard(hand, lastCard, cardStack, hasDrawnCard, playerName, direction, drawCards, saidUNO)
        if whichCard == "p" or whichCard == "P":
            if(hasDrawnCard == True):
                return lastCard
            print("Primero tiene que tomar '1' Carta")
            return playCard(hand, lastCard, cardStack, hasDrawnCard, playerName, direction, drawCards, saidUNO)
        if whichCard == "u" or whichCard == "U":
            saidUNO = True
            return playCard(hand, lastCard, cardStack, hasDrawnCard, playerName, direction, drawCards, saidUNO)
        try:
            if(canBeThrown(hand[int(whichCard)], lastCard)):
                if(drawCards[0] > 0 and (hand[int(whichCard)].getValue() != "roba2" and hand[int(whichCard)].getValue != "roba4")):
                    print("robar cartas o jugar +x Cartas!")
                    return playCard(hand, lastCard, cardStack, hasDrawnCard, playerName, direction, drawCards, saidUNO)
                thrownCard = hand.pop(int(whichCard))
                if(len(hand) == 1 and saidUNO == False):
                    print("¡Olvidaste decir UNO! - ¡Ahora tienes que sacar 1 carta!")
                    hand.append(drawCard(cardStack))
                    input("¡Presione Enter para continuar!")
                return thrownCard
            else:
                print("¡No puede ser lanzado!")
                return playCard(hand, lastCard, cardStack, hasDrawnCard, playerName, direction, drawCards, saidUNO)
        except:
            print("¡Error!")
            return playCard(hand, lastCard, cardStack, hasDrawnCard, playerName, direction, drawCards, saidUNO)


def getNames(numberOfPlayers):
    names = []
    for i in range(numberOfPlayers):
        inList = True
        while inList:
            name = input("Digite el nombre de su Jugador " + str(i + 1) + ": ")
            if name not in names:
                inList = False
            if name in names:
                print("El Nombre está en Uso: ")
        names.append(name)
    return names


def sortHand(hand):
    runs = len(hand)
    while runs >= 1:
        for i in range(len(hand) - 1):
            if hand[i + 1].color.value < hand[i].color.value:
                hand[i], hand[i + 1] = hand[i + 1], hand[i]
            elif(hand[i].color.value == hand[i + 1].color.value and hand[i + 1].value.value < hand[i].value.value):
                hand[i], hand[i + 1] = hand[i + 1], hand[i]
        runs -= 1
    return hand


def someHasEnoughtPoints(allPoints):
    i = 0
    for points in allPoints:
        if(points > 500):
            return i
        i += 1
    return -1


def initPointsOfPlayers(numberOfPlayers):
    points = []
    for i in range(numberOfPlayers):
        points.append(0)
    return points


def givePersonPoints(hands, winningPerson, pointsOfPlayers):
    points = 0
    for hand in hands:
        for card in hand:
            points += card.value.value
    pointsOfPlayers[winningPerson] += points


def getKINames(numberOfKI):
    names = []
    for i in range(numberOfKI):
        names.append("KI" + str(i))
    return names


def playCardKI(hand, lastCard, cardStack, hasDrawnCard, playerName, direction, drawCards, saidUNO):
    if(drawCards[0] > 0):
        for i in range(len(hand)):
            if hand[i].getValue() == "roba2" or hand[i].getValue() == "roba4":
                return hand.pop(i)
        for i in range(drawCards[0]):
            hand.append(drawCard(cardStack))
        return lastCard
    for i in range(len(hand)):
        if(canBeThrown(hand[i], lastCard)):
            return hand.pop(i)
    hand.append(drawCard(cardStack))
    sortHand(hand)
    for i in range(len(hand)):
        if(canBeThrown(hand[i], lastCard)):
            return hand.pop(i)
    return lastCard
