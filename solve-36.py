# Author: Peter Jensen

import sys
import itertools
import copy
import math

class Config:
  title = "--- Challenge 36: Tetonor Terror ---"
  input = "input-36.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def allPairs(grid, input):
  for c in itertools.combinations(input, 2):
    n1, n2 = c
    s = n1 + n2
    p = n1 * n2
    if s in grid and p in grid:
      yield c

def coverAll(grid, pairs):
  ps = []
  for p in pairs:
    p1, p2 = p
    ps.append(p1+p2)
    ps.append(p1*p2)
  for gn in grid:
    if gn not in ps:
      return False
  return True

def findNPairs(grid, input, n):
  if n == 0:
    return []
  else:
    pairs = []
    allPairsList = [p for p in allPairs(grid, input)]
    if 2*len(allPairsList) < len(grid):
      return []
    if not coverAll(grid, allPairsList):
      return []
    for pair in allPairs(grid, input):
      p1, p2 = pair
      p = p1*p2
      s = p1+p2
      nInput = copy.copy(input)
      nInput.pop(nInput.index(p1))
      nInput.pop(nInput.index(p2))
      nGrid = copy.copy(grid)
      nGrid.pop(nGrid.index(p))
      nGrid.pop(nGrid.index(s))
      pairs = [pair] + findNPairs(nGrid, nInput, n-1)
      if len(pairs) == n:
        return pairs
  return []

def all8Index():
  for i in itertools.combinations([i for i in range(16)], 8):
    yield i

def factors(n):
  for i in range(1, math.isqrt(n)+1):
    if n % i == 0:
      yield (i, n // i)

def prodPairs(prods, sums, n):
  if n == 0:
    yield []
  else:
    for f1, f2 in factors(prods[0]):
      if f1+f2 in sums:
        for pp in prodPairs(prods[1:], sums, n-1):
          yield [(f1, f2)] + pp

def isValid(prods, sums):
  for p8 in prodPairs(prods, sums, 8):
    sumPicks = copy.copy(sums)
    for p1, p2 in p8:
      if p1+p2 in sumPicks:
        sumPicks.pop(sumPicks.index(p1+p2))
    if len(sumPicks) == 0:
      return True
  return False

def derivedInputs(prods, sums):
  input = []
  for p in prods:
    for f1,f2 in factors(p):
      if (f1+f2) in sums:
        input.append((f1, f2))
  for i8 in itertools.combinations(input, 8):
    i8l = []
    for i1, i2 in i8:
      i8l += [i1, i2]
    i8l.sort()
    yield i8l

def inputMatch(check, input):
  for i, iv in enumerate(input):
    if iv != 0 and check[i] != iv:
      return False
  return True

def solveOne(lines):
  grid  = [int(n) for n in lines[0][2:].split(" ")]
  input = [int(n) if n != "*" else 0 for n in lines[1][2:].split(" ")]
  print(f"grid:  {grid}")
  print(f"input: {input}")
  foundPairs = None
  for i8 in all8Index():
    if foundPairs != None:
      break
    prods = [grid[i] for i in i8]
    sums  = [grid[i] for i in range(16) if i not in i8]
    if isValid(prods, sums):
#      print(prods, sums)
      for di in derivedInputs(prods, sums):
        if inputMatch(di, input):
          pairs = findNPairs(grid, di, 8) 
          if len(pairs) == 8:
            foundPairs = pairs
            print(f"resolved input: {di}")
            break
  result = 0
  for p in foundPairs:
    result += abs(p[0] - p[1])
  return result

def solve(lines):
#  for pp in prodPairs([116, 18, 56, 24, 90, 60, 100, 70], 8):
#    print(pp)
#  return
  result = 0
  for i in range(0, len(lines), 3):
    r = solveOne(lines[i:i+2])
    result += r
  print("Solution:", result)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
