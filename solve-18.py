# Author: Peter Jensen

import sys
import copy

class Config:
  title = "--- Challenge 18: Emit time ---"
  input = "input-18.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

class Time:
  secsInHour = 60*60
  secsInDay  = 24*secsInHour
  def __init__(self, hms):
    h, m, s = [int(n) for n in hms.split(":")]
    self.secs = h*self.secsInHour + m*60 + s
  def __add__(self, inc):
    self.secs += inc
    while self.secs < 0:
      self.secs += self.secsInDay
    self.secs = self.secs % self.secsInDay
    return self
  def isPalindrome(self):
    hms = self.toHMS()
    return hms[0] == hms[7] and hms[1] == hms[6] and hms[3] == hms[4]
  def toHMS(self):
    ts = self.secs % self.secsInDay
    h = ts // self.secsInHour
    ts -= h*self.secsInHour
    m = ts // 60
    ts -= m*60
    return f"{h:02}:{m:02}:{ts:02}"
  def diff(self, t):
    if self.secs < t.secs:
      return min(t.secs - self.secs, self.secs+self.secsInDay - t.secs)
    else:
      return min(self.secs - t.secs, t.secs+t.secsInDay - self.secs)

def diff(t1, t2):
  h1, m1, s1 = [int(n) for n in t1.split(":")]
  h2, m2, s2 = [int(n) for n in t2.split(":")]
  sec1 = h1*60*60 + m1*60 + s1
  sec2 = h2*60*60 + m2*60 + s2
  d = abs(sec1 - sec2)
  if sec1 < sec2:
    return min(d, abs(sec1+24*60*60 - sec2))
  else:
    return min(d, abs(sec2+24*60*60 - sec1))

def validHour(h):
  hi = int(h)
  return hi <= 23

def validMinSec(ms):
  msi = int(ms)
  return msi <= 59

def nearestPalindrome(t):
  tp = copy.copy(t)
  while not tp.isPalindrome():
    tp += 1
  tn = copy.copy(t)
  while not tn.isPalindrome():
    tn += -1
  if t.diff(tp) < t.diff(tn):
    return tp
  else:
    return tn

def solve(lines):
  dt = 0
  for l in lines:
    t = Time(l)
    np = nearestPalindrome(t)
    dt += t.diff(np)
#    print(t.toHMS(), np.toHMS(), t.diff(np))
  print("Solution: ", dt)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
