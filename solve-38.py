# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 38: Number Neighbours ---"
  input = "input-38.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def isComfy(numbers):
  return sum(numbers) % len(numbers) == 0

def isComfortable(numbers, i, l):
  nl = len(numbers)
  if l == 1:
    return True
  si = max(0, i - l + 1)
  for s in range(si, i+1):
    sr = numbers[s:s+l]
    if len(sr) == l and isComfy(numbers[s:s+l]):
      return True
  return False

def streak(numbers, i):
  for l in range(2, len(numbers)+1):
    if not isComfortable(numbers, i, l):
      return l-1
  return l

def sumStreaks(numbers):
  sum = 0
  for n in range(len(numbers)):
    sum += streak(numbers, n)
  return sum
  
def solve(lines):
  total = 0  
  for l in lines:
    total += sumStreaks([int(n) for n in l.split(" ")])
  print("Solution: ", total)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
