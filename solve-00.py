# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 00: What's a numpad? ---"
  input = "input-00.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def solve(lines):
  lookup = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz", 0: " "}
  msg = ""
  for l in lines:
    k, n = int(l[0]), int(l[2])
    msg += lookup[k][n-1]
  print("Solution:", msg)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
