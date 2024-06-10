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
#    self.hand = [c for c in hand]
    self.hand = hand
    self.__str__ = self.__repr__
  def __repr__(self):
    return self.hand
#    return "".join(self.hand)
  @staticmethod
  def flip(c):
    if c == "1":
      return "0"
    elif c == "0":
      return "1"
    return c
  def nextHands2(self):
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

  def nextHands(self):
    for i in range(len(self.hand)):
      if self.hand[i] == '1':
        nh = Hand(self.hand)
        nh.hand[i] = '.'
        if i > 0 and self.hand[i-1] != ".":
          nh.hand[i-1] = "0" if self.hand[i-1] == "1" else "1"
        if i < len(self.hand) - 1 and self.hand[i+1] != ".":
          nh.hand[i+1] = "0" if self.hand[i+1] == "1" else "1"
        yield nh
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
#    if len(key) < 1024:
     self.cache[key] = val
#    if len(self.cache) % 100 == 0:
#      print(f"cache: {self}")
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

def numSolutions(hand):
  if isinstance(hand, str):
    hand = Hand(hand)
  ns = 0
  if hand.win():
    return 1
  for nh in hand.nextHands2():
    nns = numSolutions(nh)
    if nns > 0:
      ns += 1
#  print(f"{hand}: {ns}")
  return ns

def numSolutions2(hand, cache = None):
#  print(f"mumSolutions2: {hand}, len(hand): {len(hand)}, hand.count('1'): {hand.count('1')}")
  if cache != None:
    val = cache.lookup(str(hand))
    if val != None:
      return val
  if isinstance(hand, str):
    hand = Hand(hand)
  ns = 0
  if hand.empty():
#    print(f"{hand} -> 0")
    return 0
  if hand.win():
#    print(f"{hand} -> 1")
    return 1
  for sh in str(hand).split("."):
    if sh == "":
      continue
#    print(f"sh = {sh}")
    nsh = 0
    for nh in Hand(sh).nextHands2():
      nns = numSolutions2(nh, cache)
      if nns > 0:
        nsh += 1
    if nsh == 0:
      ns = 0
      break
    else:
      ns += nsh
#  print(f"{hand}: {ns}")
  if cache != None:
    cache.insert(str(hand), ns)
#  print(f"{hand} -> {ns}")
  return ns

def hasSolutions(hand, cache = None):
  if cache != None:
    val = cache.lookup(hand)
    if val != None:
#      print(f"hasSolutions({hand}) -> {val}")
      return val
  handObj = Hand(hand)
  if handObj.empty():
#    print(f"hasSolutions({hand}) -> False")
    return False
  if handObj.win():
#    print(f"hasSolutions({hand}) -> True")
    return True
  # all subhands must have a solution
  hasSolution = True
  for sh in hand.split("."):
    if sh == "":
      continue
    shSol = False
    for nh in Hand(sh).nextHands2():
      if hasSolutions(nh, cache):
        shSol = True
        break
    if not shSol:
      hasSolution = False
      break
  if cache != None:
    cache.insert(hand, hasSolution)
#  print(f"hasSolutions({hand}) -> {hasSolution} new")
  return hasSolution

def numSolutions3(hand, cache = None):
  if isinstance(hand, str):
    hand = Hand(hand)
  ns = 0
  if hand.empty():
    return 0
  if hand.win():
    return 1
  for sh in str(hand).split("."):
    if sh == "":
      continue
    nsh = 0
    for nh in Hand(sh).nextHands2():
#      print(f"nh: {nh}")
      if hasSolutions(nh, cache):
        nsh += 1
    if nsh == 0:
      ns = 0
      break
    else:
      ns += nsh
  return ns

def hasSolutions2(hand, cache):
  if cache != None:
    val = cache.lookup(hand)
    if val != None:
#      print(f"hasSolutions2({hand}) (cache) -> {val}")
      return val
  if len(hand) == 0:
    print("ERROR")
    print(f"hasSolutions2({hand}) -> False")
    return False
  hasSolution = False
  for nh in Hand(hand).nextHands2():
#    print(f"hasSoltions2: nh = {nh}")
    nhSolution = True
    for sh in nh.split("."):
      if len(sh) > 0:
        if not hasSolutions2(sh, cache):
          nhSolution = False
          break
    if nhSolution:
      hasSolution = True
      break
  if cache != None:
    cache.insert(hand, hasSolution)
#  print(f"hasSolutions2({hand}) -> {hasSolution}")
  return hasSolution

def numSolutions4(hand, cache = None, pos = None):
  ns = 0
  if len(hand) == 0:
    print("ERROR")
    return 0
  for nh in Hand(hand).nextHands2():
    nhSolution = True
    for sh in nh.split("."):
      if len(sh) > 0 and not hasSolutions2(sh, cache):
        nhSolution = False
        break
    if nhSolution:
      if pos != None:
        pos.append(nh.find("."))
      ns += 1
  if pos != None:
    pos.sort()
  return ns

def numSolutions5(hand):
  ones = hand.count("1")
  if ones % 2 == 1:
      return ones // 2 + 1
  return 0

def solve(lines):
  nvp = 0
  cache2 = Cache()
  cache3 = Cache()
  cache4 = Cache()
#  h = "110"
#  h = "1011"
  h = "001"
#  h = "100"
#  h = "0101010110"
#  h = "000111101011110100101000111111011011011101101000110010101000011001110110010010100000000011000010000100000"
#  h = "11100001010100101110011000110111100101101010110110100100001110010001000100011100011011101000010010101100111010010010110111000111100101111110100101000101011010011001011010101111100010001101001011010110"
#  h = "000100101101011111011000011110011001110101010110110001111111110110111001111001011101111001111010001011000001010010011000011111010001000011110111100110001011000111011100011101111101000001010100001111110001000100100111001110111010001100110101001010000110100110110010010011101010101110101111110111010110001110001100011101000111101001011001011110011000111011000111110000011010001000110000110000100000000011111100011001110010101001001000110110110011111110100110000010000110000111010110111011011010001100100111111000011101000110000000110100000000101001100001011110010111111110011111010110111000101100110011110100111100111110000110000111111101001011111101111010000011101100110111010011111011101001011111001001011111000000010100100000000001110010101001000001100001111100001101101100011100111001110010110011010101000110011111001110010110111011000101001110100100001111001010100110010111111111011010110111001101"
#  print(numSolutions2(h, cache2))
#  print(numSolutions3(h, cache3))
#  print(numSolutions4(h, cache4))
#  print(numSolutions5(h))
#  print(f"cache2: {cache2}")
#  print(f"cache3: {cache3}")
#  print(f"cache4: {cache4}")
#  cache4.dump(False)
#  return

  for li, l in enumerate(lines):
#    vp1 = numSolutions(l)
#    vp2 = numSolutions2(l, cache2)
#    vp3 = numSolutions3(l, cache3)
    pos4 = []
    vp4 = numSolutions4(l, cache4, pos4)
    vp5 = numSolutions5(l)
    if vp4 != vp5:
      print(f"DIFFERENCE: {vp4} {vp5}")
      print(f"{li}: {l}: {vp4}, pos4: {pos4}, cache: {cache4}")
      break
    nvp += vp4
    print(f"{li}: {l}: {vp4}, pos4: {pos4}, cache: {cache4}")
#  cache4.dump()
  print("Solution:", nvp)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
  #cProfile.run("main()")
