# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 40: Prominence promenade ---"
  input = "input-40.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def drop(heights, pi, step):
  h = heights[pi]
  d = 0
  if step < 0:
    for i in range(pi-1, -1, -1):
      hn = heights[i]
      d = max(d, h - hn)
      if hn >= h:
        return d
    return None
  else:
    for i in range(pi+1, len(heights)):
      hn = heights[i]
      d = max(d, h - hn)
      if hn >= h:
        return d
    return None

def getP(heights, pi):
  leftDrop  = drop(heights, pi, -1)
  rightDrop = drop(heights, pi, 1)
  if leftDrop == None:
    return rightDrop if rightDrop != None else heights[pi]
  elif rightDrop == None:
    return leftDrop if leftDrop != None else heights[pi]
  else:
    return min(leftDrop, rightDrop)

def getPromTotal(heights):
  peaks = [i for i,h in enumerate(heights) if i > 0 and i < len(heights)-1 and heights[i] > heights[i-1] and heights[i] > heights[i+1]]
  promTotal = 0
  for p in peaks:
    promTotal += getP(heights, p)
  return promTotal

def solve(lines):
  heights = [int(h) for h in lines[0].split(" ")]
  print("Solution: ", getPromTotal(heights))

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
