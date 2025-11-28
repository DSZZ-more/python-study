from random import randint

class Die:
  def __init__(self, sides=6):
    self.sides = sides
  def roll_die(self):
    return randint(1, self.sides)
  
  def repeat_roll(self, times):
    for i in range(times):
      print(f"第{i+1}次：", self.roll_die())