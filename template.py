# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge xx:  ---"
  input = "input-xx.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def solve(lines):
  print("Solution: ")

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
