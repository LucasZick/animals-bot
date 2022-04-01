import random
from webbrowser import get


def getRandomAnimal():
    arquivo = open('animals.txt', 'r', encoding="utf8")
    prefixos = ['Tu é bonito igual um(a) ', 'Tu é inteligente igual um(a) ', 'Tu é chato igual um(a) ', 'Pelo menos, diferente de você, eu não sou um(a) ', 'Você me parece um(a) ', 'Sua aparência me lembra um(a) ', 'É difícil ser assim? Um(a) ']
    animals = []
    animalsReduct = []
    for linha in arquivo:
        linha = arquivo.readline()
        animals.append(linha)
    arquivo.close()
    for animal in animals:
        animalReduct = animal.split('(')
        animalsReduct.append(animalReduct[0])

    return(random.choice(prefixos) + random.choice(animalsReduct))

print(getRandomAnimal())