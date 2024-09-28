from random import randint

class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        die_rolled = randint (1,self.sides)
        print(f"The die number is {die_rolled}")


dice = Die()
dice.roll_die()