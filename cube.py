"""simulation of a die roll"""
from random import randint


class Die:
    """make a die"""
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)


s_6 = Die()
# for i in range (10):
#     s_6.roll_die()

# s_10 = Die()
# s_10.sides = 10
# for i in range (10):
#     s_10.roll_die()

s_20 = Die()
s_20.sides = 20
for i in range(10):
    s_20.roll_die()
