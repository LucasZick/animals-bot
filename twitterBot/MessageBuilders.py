import random


class RandomAnimalMessageBuilder:

    __animals__ = []

    __prefixos__ = [
        "Tu é bonito igual um(a)",
        "Tu é inteligente igual um(a)",
        "Tu é chato igual um(a)",
        "Pelo menos, diferente de você, eu não sou um(a)",
        "Você me parece um(a)",
        "Sua aparência me lembra um(a)",
        "É difícil ser assim? Um(a)"
    ]

    @staticmethod
    def add_animals(animals):
        RandomAnimalMessageBuilder.__animals__ = animals 

    @staticmethod
    def build_random_animal_message():
        prefix = random.choice(RandomAnimalMessageBuilder.__prefixos__)
        animal = random.choice(RandomAnimalMessageBuilder.__animals__)

        return f"{prefix} {animal}"

__all__ = [
    RandomAnimalMessageBuilder
]