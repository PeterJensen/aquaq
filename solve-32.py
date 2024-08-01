# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 32: In Parenthesis ---"
  input = "input-32.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

pairMap = {
  "(": ")",
  "[": "]",
  "{": "}"
}
def isBalanced(s):
  stack = []
  for c in s:
    if c in "({[":
      stack.append(c)
    elif c in ")}]":
      if len(stack) == 0:
        return False
      if c != pairMap[stack[-1]]:
        return False
      stack.pop()
  return len(stack) == 0

def solve(lines):
  bc = 0
  for l in lines:
    if isBalanced(l):
      bc += 1
  print("Solution:", bc)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
