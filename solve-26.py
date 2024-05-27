# Author: Peter Jensen

import sys
import itertools

class Config:
  title = "--- Challenge 26: Type Theft ---"
  input = "input-26.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def findNext(ns, digits):
  n = int(ns)
  if digits == 1:
    return 
  minLarger = None
  head = ns[0:len(ns) - digits]
  for p in itertools.permutations(ns[len(ns)-digits:], digits):
    nn = int(head + ''.join(p))
    if minLarger == None and nn > n:
      minLarger = nn
    if minLarger != None and nn > n and nn < minLarger:
      minLarger = nn
  return minLarger

def findMinNext(ns):
  n = int(ns)
  for d in range(2, len(ns)+1):
    nn = findNext(ns, d)
    if nn != None:
      return nn
  return n

def solve(lines):
  gain = 0
  for l in lines:
    gain += findMinNext(l) - int(l)
  print("Solution:", gain)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
