# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 01: Rose by any other name ---"
  input = "input-01.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def solve(lines):
  codes = [c if (c >= 'a' and c <= 'f') or (c >= '0' and c <= '9') else '0' for c in lines[0]]
  l = (len(codes) + 2) // 3
  groups = [codes[i:i+l] for i in range(0, 3*l, l)]
  result = groups[0][0:2] + groups[1][0:2] + groups[2][0:2]
  print("Solution:", ''.join(result))

def main():
  print(Config.title)
  lines = getLines()
#  solve(["kdb4life"])
  solve(lines)

if __name__ == "__main__":
  main()
