# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 25: S'morse ---"
  input = "input-25.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def toMs(ts):
  hms, ms = ts.split(".")
  h, m, s = hms.split(":")
  return (int(h)*60*60 + int(m)*60 + int(s))*1000 + int(ms)

morseLetterMap = {
  ".-":   "a",
  "-...": "b",
  "-.-.": "c",
  "-..":  "d",
  ".":    "e",
  "..-.": "f",
  "--.":  "g",
  "....": "h",
  "..":   "i",
  ".---": "j",
  "-.-":  "k",
  ".-..": "l",
  "--":   "m",
  "-.":   "n",
  "---":  "o",
  ".--.": "p",
  "--.-": "q",
  ".-.":  "r",
  "...":  "s",
  "-":    "t",
  "..-":  "u",
  "...-": "v",
  ".--":  "w",
  "-..-": "x",
  "-.--": "y",
  "--..": "z"
}

def toLetter(morseCode):
  return morseLetterMap[morseCode]

def getDiffs(lines):
  diffs = []
  t = toMs(lines[0])
  for l in lines[1:]:
    nt = toMs(l)
    d = nt - t
    if d not in diffs:
      diffs.append(d)
    if len(diffs) == 3:
      diffs.sort()
      diffsMap = dict()
      for i,t in enumerate([1, 3, 7]):
        diffsMap[diffs[i]] = t
      return diffsMap
    t = nt

def normalize(message, diffsMap):
  nm = [0]
  sn = 0
  st = toMs(message[0])
  pt = st
  n = 0
  for t in message[1:]:
    mst = toMs(t)
    n += diffsMap[mst - pt]
    nm.append(n)
    pt = mst
  return nm

def messages(lines, diffsMap):
  s = 0
  for i,l in enumerate(lines):
    if l == "":
      if i > s:
        yield normalize(lines[s:i], diffsMap)
      s = i+1
  if s < len(lines):
    yield normalize(lines[s:], diffsMap)

def diffs(m):
  t = m[0]
  for nt in m[1:]:
    yield nt-t
    t = nt

def decode(m):
  msg = ""
  morseCode = ""
  isSpace = False
  for d in diffs(m):
    if d == 1:
      if not isSpace:
        morseCode += '.'
    elif d == 3:
      if not isSpace:
        morseCode += '-'
      else:
        msg += toLetter(morseCode)
        morseCode = ""
    elif d == 7:
      msg += toLetter(morseCode) + " "
      morseCode = ""
    isSpace = not isSpace
  if morseCode != "":
    msg += toLetter(morseCode)
  return msg

def solve(lines):
  diffsMap = getDiffs(lines)
#  print(decode([0, 3, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 24, 25, 26, 27, 28, 31, 32, 33, 36, 37, 38, 39, 42, 45, 46, 47, 50, 51, 52, 55, 58, 59, 60, 63, 64, 65, 66, 67]))
  for m in messages(lines, diffsMap):
    print(decode(m))
  return

  print("Solution: ")

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
