# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 19: It's alive ---"
  input = "input-19.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

class Grid:
  def __init__(self, size, automatas):
    self.size = size
    self.liveOnes = set()
    for ai in range(0, len(automatas), 2):
      self.liveOnes.add(tuple(automatas[ai:ai+2]))
  def __repr__(self):
    lines = ""
    for y in range(self.size):
      line = ""
      for x in range(self.size):
        line += "#" if self.isLive((y, x)) else "."
      lines += line + "\n"
    return lines
  def isLive(self, a):
    return a in self.liveOnes
  def setState(self, a, state):
    if state:
      self.liveOnes.add(a)
    else:
      self.liveOnes.remove(a)
  def setLiveOnes(self, liveOnes):
    self.liveOnes |= liveOnes
  def setDeadOnes(self, deadOnes):
    self.liveOnes -= deadOnes
  def numLiveOnes(self):
    return len(self.liveOnes)
  def all(self):
    for y in range(self.size):
      for x in range(self.size):
        yield (y, x)
  def neighbors(self, a):
    y, x = a
    if y > 0:
      yield (y-1, x)
    if y < self.size - 1:
      yield (y+1, x)
    if x > 0:
      yield (y, x-1)
    if x <= self.size - 1:
      yield (y, x+1)
  def numLiveNeighbors(self, a):
    ln = 0
    for n in self.neighbors(a):
      if self.isLive(n):
        ln += 1
    return ln
  def hash(self):
    return hash(tuple(self.liveOnes))

def playRound(grid):
  deadOnes = set()
  liveOnes = set()
  for a in grid.all():
    nl = grid.numLiveNeighbors(a)
    if nl % 2 == 0:
      deadOnes.add(a)
    else:
      liveOnes.add(a)
  grid.setLiveOnes(liveOnes)
  grid.setDeadOnes(deadOnes)

def findCycle(hashes):
  try:
    i = hashes[0:-1].index(hashes[-1])
    return (i, len(hashes) - i - 1)
  except:
    return None
  
def playNRounds(grid, n):
  hashes = [grid.hash()]
  liveCounts = [grid.numLiveOnes()]
  for i in range(n):
    playRound(grid)
    hashes.append(grid.hash())
    liveCounts.append(grid.numLiveOnes())
    cycle = findCycle(hashes)
#    continue
    if cycle != None:
      start, repeat = cycle
      index = (n - start) % repeat + start
      return liveCounts[index]
  return grid.numLiveOnes()

def solve(lines):
  liveCount = 0
  for l in lines:
    print(f"{l}: ", end="")
    rounds, size, *liveOnes = [int(n) for n in l.split(" ")]
    grid = Grid(size, liveOnes)
    lc = playNRounds(grid, rounds)
    print(lc)
    liveCount += lc
  print("Solution: ", liveCount)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
