from inhabitant import Inhabitant
class Alien(Inhabitant):
    #a class to represent an alien
    def __init__(self, name = "Alien", age = 0, energy = Inhabitant.MAX_ENERGY):
        super().__init__(name, age, energy)
        self.technology = []

    def pickup(self, tech):
        self.technology.append(tech)

    def drop(self,tech):
        if tech in self.technology:
            self.technology.remove(tech)
    def display(self):
    print(f"I am an alien name {self.name} with technology: {self.technology}")
 if __name__ == "__main__":
     print("Testing Alien class:")
     alien = Alien(name = "Xenomorph", age= 300)
     print (repr(alien))
     print(alien)
     alien.display()
     alien.pickup("Laser")
     alien.pickup("Jetpack")
     print("After picking up technology:")
     alien.display()

     alien.drop("Laser")
     print("After dropping 'Laser': ")
     alien.display()