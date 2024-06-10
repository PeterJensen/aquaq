# Author: Peter Jensen

import sys
from copy import copy
import cProfile

class Config:
  title = "--- Challenge 30: Flip Out ---"
  input = "input-30.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

class Hand:
  def __init__(self, hand):
    self.hand = hand
    self.__str__ = self.__repr__
  def __repr__(self):
    return self.hand
  @staticmethod
  def flip(c):
    if c == "1":
      return "0"
    elif c == "0":
      return "1"
    return c
  def nextHands(self):
    l = len(self.hand)
    if l == 0:
      return
    if self.hand[0] == '1':
      if l > 1:
        yield "." + self.flip(self.hand[1]) + self.hand[2:]
      else:
        yield "."
        return
    if l > 1 and self.hand[-1] == '1':
      yield self.hand[0:-2] + self.flip(self.hand[-2]) + "."
    for i in range(1, l-1):
      if self.hand[i] == '1':
        yield self.hand[0:i-1] + self.flip(self.hand[i-1]) + "." + self.flip(self.hand[i+1]) + self.hand[i+2:]
  def empty(self):
    return len(self.hand) == 0
  def win(self):
    return self.hand.count(".") == len(self.hand)

class Cache:
  def __init__(self):
    self.hitCount = 0
    self.cache = {}
  def __repr__(self):
    return f"size: {len(self.cache)}, hitCount: {self.hitCount}"
  def insert(self, key, val):
     self.cache[key] = val
  def lookup(self, key):
    val = self.cache.get(key, None)
    if val != None:
      self.hitCount += 1
    return val
  def dump(self, val = None):
    sortedKeys = [k for k in self.cache.keys()]
    sortedKeys.sort(key=len)
    for k in sortedKeys:
      if val == None:
        if not self.cache[k]:
          print(k)
      else:
        if val == self.cache[k]:
          print(k)

def hasSolutions(hand, cache):
  if cache != None:
    val = cache.lookup(hand)
    if val != None:
      return val
  if len(hand) == 0:
    print("ERROR")
    print(f"hasSolutions2({hand}) -> False")
    return False
  hasSolution = False
  for nh in Hand(hand).nextHands():
    nhSolution = True
    for sh in nh.split("."):
      if len(sh) > 0:
        if not hasSolutions(sh, cache):
          nhSolution = False
          break
    if nhSolution:
      hasSolution = True
      break
  if cache != None:
    cache.insert(hand, hasSolution)
  return hasSolution

def numSolutions(hand, cache = None, pos = None):
  ns = 0
  if len(hand) == 0:
    print("ERROR")
    return 0
  for nh in Hand(hand).nextHands():
    nhSolution = True
    for sh in nh.split("."):
      if len(sh) > 0 and not hasSolutions(sh, cache):
        nhSolution = False
        break
    if nhSolution:
      if pos != None:
        pos.append(nh.find("."))
      ns += 1
  if pos != None:
    pos.sort()
  return ns

# Much simpler version
def numSolutions2(hand):
  ones = hand.count("1")
  if ones % 2 == 1:
    return ones // 2 + 1
  return 0

def solve(lines):
  nvp = 0
  cache = Cache()
  for li, l in enumerate(lines):
    pos = []
    vp1 = numSolutions(l, cache, pos)
#    vp2 = numSolutions2(l)
#    if vp1 != vp2:
#      print(f"DIFFERENCE: {vp1} {vp2}")
#      print(f"{li}: {l}: {vp1}, pos: {pos}, cache: {cache}")
#      break
    nvp += vp1
    print(f"{li}: {l}: {vp1}, pos: {pos}, cache: {cache}")
#  cache4.dump()
  print("Solution:", nvp)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
  #cProfile.run("main()")
