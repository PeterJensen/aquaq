# Author: Peter Jensen

import sys
import itertools

class Config:
  title = "--- Challenge 06: Let me count the ways ---"
  input = "input-06.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]


def solve(lines):
  elems = lines[0].split()
  nn, n = int(elems[0]), int(elems[5])
  found = set()
  oneCount = 0
  for cc in itertools.combinations_with_replacement(range(n+1), nn):
    if sum(cc) == n:
      for ccp in itertools.permutations(cc):
        if not ccp in found:
          found.add(ccp)  
          oneCount += "".join(map(str, ccp)).count("1")
  print("Solution:", oneCount)

def main():
  print(Config.title)
  lines = getLines()
#  solve(["3 numbers which sum to 3"])
  solve(lines)

if __name__ == "__main__":
  main()
