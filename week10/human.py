from inhabitant import Inhabitant

class Human(Inhabitant):

    def __init__(self,name = "Human", age = 0, energy = Inhabitant.MAX_ENERGY):
        super().__init__(name,age,energy)

    def __repr__(self):

        return f"Human(name = {self.name}, age={self.age}, energy={self.energy})"
    def __str__(self):

        return f"(I am {self.name},and I am {self.age} years old and my energy is {self.energy})"
    def display(self):

        print (f"I am {self.name}.")
if __name__ == "__main__":
    print("Testing human class:")
    human = Human(name="Alice",age = 30)
    print(repr(human))
    print(human)
    human.display()
