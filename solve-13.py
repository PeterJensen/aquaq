# Author: Peter Jensen

import sys
import re

class Config:
  title = "--- Challenge 13: O RLE? ---"
  input = "input-13.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def maxRepeat(s):
  mr = 0
  for i in range(len(s)-1):
    ss = s[i:]
    m = re.match(r"^(.*?)(.+?)\2+(.*)", ss)
    if m != None:
      rc = (len(ss) - len(m.group(1)) - len(m.group(3))) // len(m.group(2))
      mr = max(mr, rc)
  return mr
    
def solve(lines):
  rct = 0
  for l in lines:
    rct += maxRepeat(l)
  print("Solution:", rct)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
