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

def load_animals():
    with open('animals.txt', 'r', encoding="utf8") as file:
        animals = list(map(lambda animal: animal.split('(')[0], file.readlines()))

def get_random_animal():
    if len(animals) == 0: load_animals()
    
    return random.choice(animals)
