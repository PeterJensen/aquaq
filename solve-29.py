# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 29: On the up and up ---"
  input = "input-29.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def isGood(n):
  d = "0"
  for nd in str(n):
    if nd < d:
      return False
    d = nd
  return True

def getGoodDigits(n):
  d = "0"
  gds = ""
  for nd in str(n):
    if nd >= d:
      gds += nd
    else:
      break
    d = nd
  return gds
    
def solve(lines):
  num = int(lines[0])
#  num = 1000
  gn = 0
  n = 0
  while n <= num:
    if isGood(n):
      n += 1
      gn += 1
    else:
      numDigits = len(str(n))
      goodDigits = getGoodDigits(n)
      nextN = goodDigits + goodDigits[-1]*(numDigits-len(goodDigits))
      n = int(nextN)
  print("Solution:", gn)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
