from tkinter.font import names

from human import Human
from robot import Robot

class Planet:
    # a class to represent a planet with dictionary inhabitants
    def __init__(self,name):
    # initiate a planet object with a name a nd inhabitants dictionary
    self.name = name
    self.inhabitants = {
        "humans": [],
        "robots": []

    }
    def add_human(selfself,human)
    # add a human object to the "humans" list of the planet:
        if isinstance(human, Human):
            self.inhabitants["humans"].append(human)
        else:
            print("Error: Only Human objects can be added.")
    def add_robot(self):
    # Add a robot to the 'robots' list of the Planet.
        if isinstance(robot,Robot)
        self.inhabitants["robots"].append(robot)
        else:
        print("Error: Only Robot objects can be added.")
    def __repr__ (self):
        return f"Planet(name={self.name}, inhabitants={self.inhabitants})"
    def __str__ (self):
        return (
            f"Planet {self.name}:\n"
            f"Humans {[str(human) for human in self.inhabitants["humans]]}\n"
            f"robots {[str(robot)for robot ]}"
        )
if __name__ == "__main__":
    print("Testing Planet class:")
    earth = Planet(name = "Earth" )
    human1 = Human(name = "Alice", age = 25)
