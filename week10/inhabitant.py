from abc import ABC, abstractmethod

class Inhabitant(ABC):

    MAX_ENERGY = 100

    def __init__(self, name = "Inhabitant", age = 0, energy = MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = energy
    @abstractmethod
    def display(self):

        pass
    def __repr__(self):

        return f"Inhabitant(name{self.name} age{self.age} energy{self.energy}."
    def __str__(self):

        return f"{self.name} is {self.age} years old with {self.energy} energy."
