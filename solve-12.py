# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 12: A Day In The Lift ---"
  input = "input-12.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def solve(lines):
  moves = [tuple(map(int, l.split())) for l in lines]
  floor = 0
  visits = 1
  dir = 1
  while floor >= 0 and floor < len(moves):
#    print(f"floor: {floor}")
    m = moves[floor]
    if m[0] == 0:
      dir *= -1
    floor += dir*m[1]
    visits += 1
  print("Solution:", visits)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
