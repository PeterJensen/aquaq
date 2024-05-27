# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 21: Clean Sweep ---"
  input = "input-21.txt"
  width = 5

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

class Tiles:
  def __init__(self, lines):
    self.rows = []
    for l in lines:
      self.rows.append([int(t) for t in l.split(" ")])
  def row(self, ri):
    return self.rows[ri]
  def numRows(self):
    return len(self.rows)
  def __repr__(self):
    def rs(row):
      return "".join([f"{t:4}" for t in row])
    return "\n".join([rs(r) for r in self.rows])

def solve(lines):
  tiles = Tiles(lines)
  rl = len(tiles.row(0))
  maxMotes = [[0 for _ in range(rl-Config.width+1)] for _ in range(tiles.numRows())]
  for ri in range(tiles.numRows()-1, -1, -1):
    r = tiles.row(ri)
    mnl = len(maxMotes[ri])
    for ti in range(mnl):
      motes = sum(r[ti:ti + Config.width])
      if ri < tiles.numRows()-1:
        if ti == 0:
          mns = 0
          mne = 1
        elif ti < mnl-1:
          mns = ti-1
          mne = ti+1
        else:
          mns = ti-1
          mne = ti
        motes += max(maxMotes[ri+1][mns:mne+1])
      maxMotes[ri][ti] = motes
  #print(maxMotes)
  print("Solution: ", max(maxMotes[0]))

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
