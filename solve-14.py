# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 14: That's a bingo ---"
  input = "input-14.txt"
  board = [[6, 17, 34, 50, 68],
           [10, 21, 45, 53, 66],
           [5,  25, 36, 52, 69],
           [14, 30, 33, 54, 63],
           [15, 23, 41, 51, 62]]

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def isMatch(nums, checkNums):
  return len(set(checkNums) - set(nums)) == 0

def bingo(nums, board):
  for r in range(5):
    if isMatch(nums, board[r]):
      return True
  for c in range(5):
    bc = []
    for r in range(5):
      bc.append(board[r][c])
    if isMatch(nums, bc):
      return True
  bd1 = []
  bd2 = []
  for i in range(5):
    bd1.append(board[i][i])
    bd2.append(board[4-i][i])
  if isMatch(nums, bd1) or isMatch(nums, bd2):
    return True
  return False

def getMinNums(allNums, board):
  for n in range(5, len(allNums)):
    if bingo(allNums[0:n], board):
      return n
  return None

def solve(lines):
  total = 0
  for l in lines:
    nums = [int(n) for n in l.split(" ")]
    total += getMinNums(nums, Config.board)
  print("Solution: ", total)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
