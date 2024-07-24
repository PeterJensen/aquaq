# Author: Peter Jensen

import sys
import copy

class Config:
  title = "--- Challenge 05:  ---"
  input = "input-05.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

class Dice:
  def __init__(self, faces):
    self.faces = copy.copy(faces)
    self.faces["A"] = 7 - self.faces["F"] # "A" == bAck
    self.faces["B"] = 7 - self.faces["T"]
    self.faces["R"] = 7 - self.faces["L"]
  def __repr__(self):
    return f"{self.faces}"
  def turn(self, dir):
    faces = copy.copy(self.faces)
    if dir == "L":
      for f, t in zip("FLTABR", "LATRBF"):
        self.faces[t] = faces[f]
    elif dir == "R":
      for f, t in zip("FLTABR", "RFTLBA"):
        self.faces[t] = faces[f]
    elif dir == "U":
      for f, t in zip("FLTABR", "TLABFR"):
        self.faces[t] = faces[f]
    elif dir == "D":
      for f, t in zip("FLTABR", "BLFTAR"):
        self.faces[t] = faces[f]
  def front(self):
    return self.faces["F"]

def solve(lines):
  dice1 = Dice({'F': 1, 'L':2, 'T':3})
  dice2 = Dice({'F': 1, 'L':3, 'T':2})
  sum = 0
  for i,m in enumerate(lines[0]):
    dice1.turn(m)
    dice2.turn(m)
    if dice1.front() == dice2.front():
      sum += i
  print("Solution:", sum)

def main():
  print(Config.title)
  lines = getLines()
#  solve(["LRDLU"])
  solve(lines)

if __name__ == "__main__":
  main()
