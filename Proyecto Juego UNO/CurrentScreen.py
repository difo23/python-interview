import os
from EnumsCards import *


def showToDrawnCards(drawCards):
    print("+Cartas: " + str(drawCards[0]) + "\t", end="")


def showDirection(direction):
    if(direction == 1):
        print("Dirección: Agujas del Reloj\t", end="")
    else:
        print("Dirección: C-Agujas del Reloj\t", end="")


def showHand(hand):
    whichCard = 0
    for card in hand:
        print("" + str(card.getValue()) + " " +
              str(card.getColor()) + " \t\t-->    " + str(whichCard))
        whichCard += 1


def showOptions(hand):
    print()
    print("Pasar -> P")
    print("Tomar Carta(s) -> D")
    if(len(hand) == 2):
        print("¡UNO! -> U")


def showCurrentScreen(hand, direction, lastCard, playerName, drawCards):
    clearScreen()
    showPlayerName(playerName)
    showDirection(direction)
    showToDrawnCards(drawCards)
    showLastCard(lastCard)
    showHand(hand)
    showOptions(hand)


def showPlayerName(playerName):
    print("Nombre: " + playerName + "\t", end="")


def showLastCard(lastCard):
    print("Carta en Mesa: " + str(lastCard.getValue()) +
          " " + str(lastCard.getColor()))


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


def showChooseColorScreen(startMessage, hand, direction, lastCard, playerName, drawCards):
    clearScreen()
    showPlayerName(playerName)
    showDirection(direction)
    showToDrawnCards(drawCards)
    showLastCard(lastCard)
    showHand(hand)
    print(startMessage)
    print("Selecciones el Nuevo Color:")
    print("Azul\t\t->\tb")
    print("Rojo\t\t->\tr")
    print("Amarillo\t->\ty")
    print("Verde\t\t->\tg")
    newColor = input().lower()
    if(newColor == "b"):
        return 0
    elif(newColor == "r"):
        return 1
    elif(newColor == "y"):
        return 2
    elif(newColor == "g"):
        return 3
    else:
        return showChooseColorScreen("¡No es un Color!")


def showPointsOfPlayers(pointsOfPlayers, names):
    i = 0
    for points in pointsOfPlayers:
        print("Puntos de " + names[i] + ": " + str(pointsOfPlayers[i]))
        i += 1
