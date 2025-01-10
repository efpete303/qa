# from types import new_class
#
#
# class Human:
#     """
#     presents human with attributes
#     """
#     MAX_ENERGY = 100
#     def __init__(self):
#         self.name = "Human"
#         self.age = 0
#         self.energy = Human.MAX_ENERGY
#     def display(self):
#         print(f" I am {self.name}")
# if __name__ == "__main__":
#     human = Human()
#     human.display()

# class Robot:
#     def __init__(self):
#         self.name = "Robot"
#         self.model = "Generic"
#         self.energy = 0
#     def display(self):
#         print(f"I am {self.name}")
#
# if __name__ == "__main__":
#     robot = Robot()
#     robot.display()
#

# class Human:
#     """
#     presents human with attributes
#     """
#     MAX_ENERGY = 100
#     def __init__(self):
#         self.name = "Human"
#         self.age = 0
#         self.energy = Human.MAX_ENERGY
#     def display(self):
#         print(f" I am {self.name}")
#     def grow(self):
#         self.age +=1
#     def eat(self, ammount):
#         self.energy = min (self.energy + ammount, Human.MAX_ENERGY)
# if __name__ == "__main__":
#     human = Human()
#     human.display()

class Robot:
   """
   A class to represent a Robot with attributes for name, model, and energy.
   """

   # Class attribute (constant)
   MAX_ENERGY = 100

   def __init__(self):
       """
       Initialize a Robot object with default name, model, and energy.
       """
       self.name = "Robot"
       self.model = "Generic"
       self.energy = 0

   def grow(self):
       """
       Increase the "age" (or lifespan equivalent) of the robot by 1.
       """
       print(f"Robot {self.name} has grown by 1 lifespan unit.")  # Robots might not have 'age' explicitly

   def eat(self, amount):
       """
      Increase the energy of the robot by the given amount, without exceeding MAX_ENERGY.
       """
       self.energy = min(self.energy + amount, Robot.MAX_ENERGY)

   def move(self, distance):
       """
       Decrease the energy of the robot by the given distance, ensuring energy does not fall below 0.
       """
       self.energy = max(self.energy - distance, 0)

   def display(self):
       """
       Display the name of the robot in the format "I am {name}".
       """
       print(f"I am {self.name}")

   def __repr__(self):
       """
       Return a formal string representation of the Robot object.
       """
      return f"Robot(name={self.name}, model={self.model}, energy={self.energy})"

   def __str__(self):
       """
       Return an informal string representation of the Robot object.
       """
       return f"Robot {self.name} is of model {self.model} with {self.energy} energy."


# Testing the Robot class
if __name__ == "__main__":
   robot = Robot()
   robot.display()
   robot.eat(50)
   robot.move(20)
   print(robot)  # Informal representation
   print(repr(robot))  # Formal representation