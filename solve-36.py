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

def pairCombos(nums):
  return itertools.combinations(nums, 2)

def getPairs(grid, input):
  good = []
  gridCounts  = {k:grid.count(k) for k in grid}
  inputCounts = {k:input.count(k) for k in input}
  for c in itertools.combinations(input, 2):
    n1, n2 = c
    s = n1 + n2
    p = n1 * n2
    if (s == p and gridCounts.get(s, 0) > 1) or (s != p and gridCounts.get(s, 0) > 0 and gridCounts.get(p, 0) > 0):
      if n1 == n2:
        if inputCounts[n1] > 1:
          good.append(c)
          inputCounts[n1] -= 2
          gridCounts[s] -= 1
          gridCounts[p] -= 1
      elif inputCounts[n1] > 0 and inputCounts[n2] > 0:
        good.append(c)
        inputCounts[n1] -= 1
        inputCounts[n2] -= 1
        gridCounts[s] -= 1
        gridCounts[p] -= 1
  return good

def allPairs(grid, input):
  for c in itertools.combinations(input, 2):
    n1, n2 = c
    s = n1 + n2
    p = n1 * n2
    if s in grid and p in grid:
      yield c

def getAllPairs(grid, input):
  return {p for p in allPairs(grid, input)}

def all8PairCombos(grid, input):
#  for p8 in itertools.combinations(allPairs(grid, input), 8):
  for p8 in itertools.combinations(getAllPairs(grid, input), 8):
    yield p8

def getAll8PairCombos(grid, input):
  return {p8 for p8 in all8PairCombos(grid, input)}

def getCombos(b, e, n):
  return sorted(list(set([tuple(sorted(c)) for c in itertools.product(range(b,e+1), repeat=n)])))

def starRanges(input):
  i = 0
  b = 1
  e = 0
  n = 0
  while i < len(input):
    if input[i] == 0:
      n += 1
    else:
      if n > 0:
        b = input[i-n-1] if i-n-1 > 0 else 1
        e = input[i]
        yield (b, e, n)
      n = 0
    i += 1
  if input[-1] == 0:
    b = input[-n-1] if n < len(input) else 1
    e = b
    yield (b, e, n)

def getStarRanges(input):
  return [sr for sr in starRanges(input)]

def allCombos(input):
  combos = []
  for b, e, n in starRanges(input):
    combos.append(getCombos(b, e, n))
  for p in itertools.product(*combos):
    t = tuple()
    for e in p:
      t += e
    yield t

def allInputs(input):
  for c in allCombos(input):
    i = [n for n in input]
    for sc in c:
      i[i.index(0)] = sc
    yield i
    
def getInputs(input):
  return [i for i in allInputs(input)]

def allPairsWithIndex(grid, inputIndex):
  for pair in itertools.combinations(inputIndex, 2):
    ni1, ni2 = pair
    n1, n2 = ni1[1], ni2[1]
    s = n1 + n2
    p = n1 * n2
    if s in grid and p in grid:
      yield pair

def getMappings(grid, input):
  map = {}
#  for pair in allPairsWithIndex(grid, [(i, v) for i, v in enumerate(input)]):
  for pair in allPairs(grid, input):
    ni1, ni2 = pair
#    n1, n2 = ni1[1], ni2[1]
    n1, n2 = ni1, ni2
    s = n1 + n2
    p = n1 * n2
    map[s] = map.get(s, set()) | {pair}
    map[p] = map.get(p, set()) | {pair}
  for k in sorted(map.keys()):
    print(f"{k}({grid.count(k)}): {map[k]}")
  pairs = []
  for k, v in map.items():
    if len(v) == 1 :
      print(v)
      p = list(v)[0]
      pairs.append(p)
      map[k] = set()
  print(pairs)
  for k in sorted(map.keys()):
    print(f"{k}({grid.count(k)}): {map[k]}")

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

def all8(grid):
  for prods in itertools.combinations(grid, 8):
    yield prods

def all8Index():
  for i in itertools.combinations([i for i in range(16)], 8):
    yield i

def factors(n):
  for i in range(1, math.isqrt(n)+1):
    if n % i == 0:
      yield (i, n // i)

def isValid(prods, sums):
  prodPairs = []
  for p in prods:
    for f1, f2 in factors(p):
      if (f1 + f2) in sums:
        prodPairs.append((f1, f2))
  for p8 in itertools.combinations(prodPairs, 8):
    sumPicks = copy.copy(sums)
    for p1, p2 in p8:
      if p1+p2 in sumPicks:
        sumPicks.pop(sumPicks.index(p1+p2))
    if len(sumPicks) == 0:
      return True
  return False

def deriveInput(prods, sums):
  input = []
  for p in prods:
    for f1,f2 in factors(p):
      if (f1+f2) in sums:
        input += [f1, f2]
        break
  input.sort()
  return input

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
      print(prods, sums)
      for di in derivedInputs(prods, sums):
        if inputMatch(di, input):
          pairs = findNPairs(grid, di, 8) 
          if len(pairs) == 8:
            foundPairs = pairs
            print(di)
            break
  result = 0
  for p in foundPairs:
    result += abs(p[0] - p[1])
  return result

def solve(lines):
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
