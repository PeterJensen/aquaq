# Author: Peter Jensen

import sys
import string

class Config:
  title   = "--- Challenge 23: Fair Play ---"
  input   = "input-23.txt"
  keyword = "power plant"
#  keyword = "playfair"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

class Enigma:
  def __init__(self, kw):
    self.grid = self._getGrid(kw)
    self.xyGrid = self._getXyGrid(self.grid)

  @staticmethod
  def _getGrid(kw):
    gridStr = ""
    for c in kw:
      if c not in gridStr and c != ' ':
        gridStr += c
    for c in string.ascii_lowercase:
      if c not in gridStr and c != 'j':
        gridStr += c
    grid = []
    for i in range(0, 25, 5):
      grid.append(gridStr[i:i+5])
    return grid

  @staticmethod
  def _getXyGrid(grid):
    xyGrid = {}
    for x in range(5):
      for y in range(5):
        xyGrid[grid[y][x]] = (x, y)
    return xyGrid

  def _charAt(self, xy):
    x, y = xy
    return self.grid[y][x]

  def _xyFor(self, c):
    return self.xyGrid[c]

  def _encryptPair(self, pair):
    x0, y0 = self._xyFor(pair[0])
    x1, y1 = self._xyFor(pair[1])
    if y0 == y1:
      return self._charAt(((x0 + 1) % 5, y0)) + self._charAt(((x1 + 1) % 5, y1))
    elif x0 == x1:
      return self._charAt((x0, (y0 + 1) % 5)) + self.charAt((x1, (y1 + 1) % 5))
    else:
      return self._charAt((x1, y0)) + self._charAt((x0, y1))

  def _decryptPair(self, pair):
    x0, y0 = self._xyFor(pair[0])
    x1, y1 = self._xyFor(pair[1])
    if y0 == y1:
      xl0 = x0 - 1 if x0 > 0 else 4
      xl1 = x1 - 1 if x1 > 0 else 4
      return self._charAt((xl0, y0)) + self._charAt((xl1, y1))
    elif x0 == x1:
      yu0 = y0 - 1 if y0 > 0 else 4
      yu1 = y1 - 1 if y1 > 0 else 4
      return self._charAt((x0, yu0)) + self._charAt((x1, yu1))
    else:
      return self._charAt((x1, y0)) + self._charAt((x0, y1))

  def encrypt(self, s):
    es = s[0]
    for i in range(1, len(s), 1):
      if s[i-1] == s[i]:
        es += 'x'
      es += s[i]
    if len(es) % 2 != 0:
      es += 'x'
    nes = ""
    for i in range(0, len(es), 2):
      nes += self._encryptPair(es[i:i+2])
    return nes

  def decrypt(self, s):
    ds = ""
    for i in range(0, len(s), 2):
      ds += self._decryptPair(s[i:i+2])
    return ds

def solve(lines):
  enigma = Enigma(Config.keyword)
  print("Solution:", enigma.decrypt(lines[0]))

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
