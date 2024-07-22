# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 02: One is all you need ---"
  input = "input-02.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def solve(lines):
  nums = [int(n) for n in lines[0].split(" ")]
  newNums = []
  for i,n in enumerate(nums):
    if n in newNums:
      ni = newNums.index(n)
      newNums = newNums[0:ni]
    newNums.append(n)
  print("Solution:", sum(newNums))

def main():
  print(Config.title)
  lines = getLines()
#  solve(["1 4 3 2 4 7 2 6 3 6"])
  solve(lines)

if __name__ == "__main__":
  main()
