# Author: Peter Jensen

import sys
import copy

class Config:
  title = "--- Challenge 31: Brandless Combination Cubes ---"
  input = "input-31.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

class Dir:
  clockwise     = 0
  antiClockwise = 1
  toString      = ["clockwise", "antiClockwise"]

class Cube:
  test = False
  def __init__(self):
    if self.test:
      self.surfaces = {
        'F': [[1,2,3], [4,5,6], [7,8,9]],
        'U': [[1,2,3], [4,5,6], [7,8,9]],
        'L': [[1,2,3], [4,5,6], [7,8,9]],
        'R': [[1,2,3], [4,5,6], [7,8,9]],
        'D': [[1,2,3], [4,5,6], [7,8,9]],
        'B': [[1,2,3], [4,5,6], [7,8,9]]
      }
    else:
      self.surfaces = {
        'F': [[1,1,1], [1,1,1], [1,1,1]],
        'U': [[2,2,2], [2,2,2], [2,2,2]],
        'L': [[3,3,3], [3,3,3], [3,3,3]],
        'R': [[4,4,4], [4,4,4], [4,4,4]],
        'D': [[5,5,5], [5,5,5], [5,5,5]],
        'B': [[6,6,6], [6,6,6], [6,6,6]]
      }
  def __repr__(self):
    f = self.faceStr("F").split("\n")
    u = self.faceStr("U").split("\n")
    l = self.faceStr("L").split("\n")
    r = self.faceStr("R").split("\n")
    d = self.faceStr("D").split("\n")
    b = self.faceStr("B").split("\n")
    s = ""
    for row in u:
      s += " "*4 + row + "\n"
    s += "\n"
    for lr, fr, rr in zip(l, f, r):
      s += lr + " " + fr + " " + rr + "\n"
    s += "\n"
    for row in d:
      s += " "*4 + row + "\n"
    s += "\n"
    for row in b:
      s += " "*4 + row + "\n"
    return s
  def faceStr(self, surface):
    s = ""
    for r in range(3):
      if s != "":
        s += "\n"
      s += "".join([str(c) for c in self.surfaces[surface][r]])
    return s
  def getSurface(self, srf):
    return self.surfaces[srf]
  def getRow(self, srf, ri):
    return copy.copy(self.surfaces[srf][ri])
  def getCol(self, srf, ci):
    return [self.surfaces[srf][ri][ci] for ri in range(3)]
  def setRow(self, srf, ri, row):
    self.surfaces[srf][ri] = row
  def setCol(self, srf, ci, col):
    for ri in range(3):
      self.surfaces[srf][ri][ci] = col[ri]
  def rotateSurface(self, srf, dir):
    r0, c0, r2, c2 = self.getRow(srf, 0), self.getCol(srf, 0), self.getRow(srf, 2), self.getCol(srf, 2)
#    if srf in "B":
#      dir = Dir.clockwise if dir == Dir.antiClockwise else Dir.antiClockwise
    if dir == Dir.clockwise:
      self.setCol(srf, 2, r0)
      self.setRow(srf, 2, c2[::-1])
      self.setCol(srf, 0, r2)
      self.setRow(srf, 0, c0[::-1])
    else:
      self.setCol(srf, 0, r0[::-1])
      self.setRow(srf, 0, c2)
      self.setCol(srf, 2, r2[::-1])
      self.setRow(srf, 2, c0)
  @staticmethod
  def rotateEdges(edges, dir):
    e0, e1, e2, e3 = [copy.copy(edges[i]) for i in range(4)]
    if dir == Dir.clockwise:
      edges[0] = e3[::-1]
      edges[1] = e0
      edges[2] = e1[::-1]
      edges[3] = e2
    else:
      edges[0] = e1
      edges[1] = e2[::-1]
      edges[2] = e3
      edges[3] = e0[::-1]
  def getRowOrCol(self, code):
    srf, roc, rci = code[0], code[1], int(code[2])
    if roc in "rR":
      rc = self.getRow(srf, rci)
    else:
      rc = self.getCol(srf, rci)
    if roc in "rc":
      rc = rc[::-1]
    return rc
  def setRowOrCol(self, code, rc):
    srf, roc, rci = code[0], code[1], int(code[2])
    if roc in "rc":
      rc = rc[::-1]
    if roc in "rR":
      self.setRow(srf, rci, rc)
    else:
      self.setCol(srf, rci, rc)
  def rotate(self, srf, dir):
    trans = {"U": ["BR2", "Rr0", "FR0", "LR0"],
             "L": ["UC0", "FC0", "Dc0", "Bc0"],
             "B": ["DR2", "Rc2", "UR0", "Lc0"],
             "R": ["Uc2", "Bc2", "DC2", "FC2"],
             "F": ["UR2", "RC0", "DR0", "LC2"],
             "D": ["FR2", "RR2", "BR0", "Lr2"]}
    self.rotateSurface(srf, dir)
    src = trans[srf]
    edges = [self.getRowOrCol(c) for c in src]
    self.rotateEdges(edges, dir)
    for i, s in enumerate(src):
      self.setRowOrCol(s, edges[i])

def solve(lines):
  cube = Cube()
  print(cube)
#  cube.rotate("U", Dir.clockwise)
#  cube.rotate("U", Dir.antiClockwise)
#  cube.rotate("L", Dir.clockwise)
#  cube.rotate("L", Dir.antiClockwise)
#  cube.rotate("B", Dir.clockwise)
#  cube.rotate("B", Dir.antiClockwise)
#  cube.rotate("R", Dir.clockwise)
#  cube.rotate("R", Dir.antiClockwise)
#  cube.rotate("F", Dir.clockwise)
#  cube.rotate("F", Dir.antiClockwise)
#  cube.rotate("D", Dir.clockwise)
#  cube.rotate("D", Dir.antiClockwise)
#  print(cube)
#  return
#  cmds = "U'LBRU"
  cmds = lines[0]
  for ci, c in enumerate(cmds):
    dir = Dir.clockwise
    if c == "'":
      continue
    if ci < len(cmds) - 1 and cmds[ci+1] == "'":
      dir = Dir.antiClockwise
    surface = c
    cube.rotate(surface, dir)
  print(cube)
  front = cube.getSurface("F")
  p = 1
  for ri in range(3):
    for ci in range(3):
      p *= front[ri][ci]
  print("Solution:", p)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
