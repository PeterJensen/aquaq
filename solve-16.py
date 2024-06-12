# Author: Peter Jensen

import sys
import string

class Config:
  title = "--- Challenge 16: Keming ---"
  input = "input-16.txt"
  letters = "asciialphabet.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def getLetters():
  return [l.rstrip("\n\r") for l in open(Config.letters, 'r').readlines()]

class Letters:
  pairs   = {'LT': 10, 'TA': 10}
  def __init__(self, letters):
    self.letters = {}
    self.singles = {}
    self.numDots = {}
    for l in string.ascii_uppercase:
      i = (ord(l) - ord('A'))*6
      self.letters[l] = letters[i:i+6]
      self.singles[l] = max([len(ll) for ll in self.letters[l]])
      self.numDots[l] = sum([ll.count("#") for ll in self.letters[l]])
  def pairWidth(self, pair):
    p1, p2 = pair
    l1, l2 = self.letters[p1], self.letters[p2]
    ml = 0
    for i in range(6):
      l = len(l1[i].rstrip()) + 1 + len(l2[i].lstrip())
      ml = max(ml, l)
    return ml
  def singleWidth(self, letter):
    return self.singles[letter]
  def nonSpaces(self, letter):
    return self.numDots[letter]

def solve(lines):
  letters = Letters(getLetters())
  line = lines[0]
#  line = "LTA"
  totalWidth = letters.singleWidth(line[0])
  nonSpaces = letters.nonSpaces(line[0])
  for ci in range(1, len(line)):
    pair = line[ci-1:ci+1]
    totalWidth += letters.pairWidth(pair) - letters.singleWidth(pair[0])
    nonSpaces += letters.nonSpaces(pair[1])
  print("Solution:", totalWidth*6 - nonSpaces)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
