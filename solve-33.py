# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 33:  ---"
  input = "input-33.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def getDartValues():
  dvs = set()
  for v in range(1,21):
    dvs.add(v)
    dvs.add(2*v)
    dvs.add(3*v)
  dvs.add(25)
  dvs.add(50)
  dvl = list(dvs)
  dvl.sort()
  return dvl

class Cache:
  maxVal = 200
  def __init__(self):
    self.cache = {}
  def add(self, val, res):
    if val < self.maxVal:
      self.cache[val] = res
  def lookup(self, val):
    if val < self.maxVal:
      return self.cache.get(val, None)
    return None

def numDarts(val, dvl, cache = None):
  if cache != None:
    nd = cache.lookup(val)
    if nd != None:
      return nd, None
  if val == 0:
#    return 0, []
    if cache != None:
      cache.add(0, 0)
    return 0, None
  if val in dvl:
#    return 1, [val]
    if cache != None:
      cache.add(val, 1)
    return 1, None
  maxDv = dvl[-1]
  for i in range(len(dvl)-1, -1, -1):
    if dvl[i] <= val:
      maxDv = dvl[i]
      break
  if val < dvl[-1]:
    nd, vl = numDarts(val - maxDv, dvl, cache)
#    return 1 + nd, [maxDv] + vl
    if cache != None:
      cache.add(val, 1 + nd)
    return 1 + nd, None
  else:
    minNd = None
    for i in range(len(dvl)-1, -1, -1):
      dv = dvl[i]
      if dv < 21:
        break
      ndMax = val // dv
      if ndMax > 1:
        ndMax -= 1
      nd, vl = numDarts(val - ndMax*dvl[i], dvl, cache)
      if minNd == None or ndMax + nd < minNd:
        minNd = ndMax + nd
#        minVl = [f"{ndMax}*{dvl[i]}"] + vl
#    return minNd, minVl
    if cache != None:
      cache.add(val, minNd)
    return minNd, None

def test():
  dvl = getDartValues()
  print(dvl)
  for i in range(1,500):
    print(f"{i}: {numDarts(i, dvl)}")

def solve(lines):
#  test()
#  return
  dvl = getDartValues()
#  num = 30
  num = int(lines[0])
  sumNd = 0
  cache = Cache()
  for n in range(1,num+1):
    nd, _ = numDarts(n, dvl, cache)
    if n % 1000 == 0:
      print(f"{n}: {nd}")
    sumNd += nd
  print("solution:", sumNd)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
