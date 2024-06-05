# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 08: Cron Flakes ---"
  input = "input-08.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

class Ingredients:
  def __init__(self):
    self.milk = []
    self.cereal = 0
  def __repr__(self):
    return f"milk: {self.milk}\ncereal: {self.cereal}"
  def canEat(self):
    return len(self.milk) > 0 and self.milk[0][0] >= 100 and self.cereal >= 100
  def buyMilk(self, amount):
    if amount > 0:
      self.milk.append([amount, 5])
  def buyCereal(self, amount):
    self.cereal += amount
  def eat(self):
    if self.canEat():
      self.milk[0][0] -= 100
      self.cereal -= 100
      if self.milk[0][0] == 0:
        self.milk.pop(0)
  def nextDay(self):
    for i in range(len(self.milk)):
      self.milk[i][1] -= 1
    if len(self.milk) > 0 and self.milk[0][1] < 0:
      self.milk.pop(0)
  def getTotals(self):
    t = 0
    for m in self.milk:
      t += m[0]
    return t + self.cereal

def solve(lines):
  mc = Ingredients()
  for l in lines[1:]:
    milk, cereal = [int(n) for n in l.split(",")[1:]]
    mc.buyCereal(cereal)
    mc.eat()
    mc.buyMilk(milk)
    mc.nextDay()
  print("Solution:", mc.getTotals())
  
def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
