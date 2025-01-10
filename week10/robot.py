from inhabitant import Inhabitant
class Robot(Inhabitant):
    # a class to represent a Robot, inheriting from Inhabitant.
    # class attribute (list of Robot laws)
    laws = [
        "A robot may not harm a human being. "
        "A robot must obey orders given by humans. "
        "A robot must protect its own existence. "

    ]
    def __init__(self, name = "Robot",age = 0, model = "Generic", energy = Inhabitant.MAX_ENERGY):
        super().__init__(name =name)
        self.model = model
    def display(self):
        print(f"I am {self.name}.")
    @staticmethod
    def the_laws():
        return robot.laws
    def __repr__(self):
        return f"Robot(name= {self.name},model={self.model}, age={self.age},energy={self.energy})"
    def __str__(self):
        return f"Robot(name= {self.name},model={self.model}, age={self.age},energy={self.energy})"
if __name__ == "__main__":
    print("testing robot class")
    robot = Robot(name="Robot",model="X108",energy =45,age =15)
    print(repr(robot))
    robot.display()
    print("Robot laws:")
    for law in Robot.the_laws():
        print(f"- {law}")