# Author: Peter Jensen

import sys
import math

class Config:
  title = "--- Challenge 04: This is good co-primen ---"
  input = "input-04.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def factors(n):
  for i in range(1, math.isqrt(n)+1):
    if n % i == 0:
      yield (i, n // i)

def getFactors(n):
  nFactors = set()
  for f1, f2 in factors(n):
    if f1 > 1: nFactors.add(f1)
    if f2 > 1: nFactors.add(f2)
  return nFactors

def coPrimes(num):
  numFactors = getFactors(num)
  for n in range(1, num):
    useN = True
    for f1, f2 in factors(n):
      if f1 in numFactors or f2 in numFactors:
        useN = False
        break
    if useN:
      yield n

def solve(lines):
  num = int(lines[0])
  sum = 0
  for cp in coPrimes(num):
    sum += cp
  print("Solution:", sum)

def main():
  print(Config.title)
  lines = getLines()
#  solve(["15"])
  solve(lines)

if __name__ == "__main__":
  main()
