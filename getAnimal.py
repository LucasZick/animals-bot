import random
from webbrowser import get


def getRandomAnimal():
    arquivo = open('animals.txt', 'r', encoding="utf8")
    animals = []
    for linha in arquivo:
        linha = arquivo.readline()
        animals.append(linha)
    arquivo.close()

    return('Tu é inteligente igual um(a) ' + random.choice(animals))
