# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 09: Big Data? ---"
  input = "input-09.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def solve(lines):
  p = 1
  for l in lines:
    p *= int(l)
  print("Solution: ", p)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
