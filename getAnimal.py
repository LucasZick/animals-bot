import random


prefixos = [
    'Tu é bonito igual um(a) ',
    'Tu é inteligente igual um(a) ',
    'Tu é chato igual um(a) ',
    'Pelo menos, diferente de você, eu não sou um(a) ',
    'Você me parece um(a) ',
    'Sua aparência me lembra um(a) ',
    'É difícil ser assim? Um(a) '
]

animals = []

def getRandomAnimal():
    with open('animals.txt', 'r', encoding="utf8") as file:
        animals = list(map(lambda animal: animal.split('(')[0], file.readlines()))

    return(random.choice(prefixos) + random.choice(animals))
