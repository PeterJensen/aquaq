# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 22: Veni Vidi Vitavi ---"
  input = "input-22.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def toRoman(num):
  letters = [
    'M', 'CM', 'D', 'CD',
    'C', 'XC', 'L', 'XL',
    'X', 'IX', 'V', 'IV',
    'I'
  ]
  lookupValues = [
    1000, 900, 500, 400,
     100,  90,  50,  40,
      10,   9,   5,   4,
       1
  ]
  result = '';
  index = 0
  while num > 0:
    while num >= lookupValues[index]:
      num -= lookupValues[index]
      result += letters[index]
    index += 1
  return result;

def encode(n):
  rn = toRoman(n)
  dn = 0
  for rc in rn:
    dn += ord(rc) - ord("A") + 1
  return dn

def solve(lines):
  nums = [int(n) for n in lines[0].split()]
  sum = 0
  for n in [int(n) for n in nums]:
#    print(f"{n} = {toRoman(n)}: {encode(n)}")
    sum += encode(n)
  print("Solution:", sum)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
