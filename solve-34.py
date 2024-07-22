# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 34: Train in Vain ---"
  input = "input-34.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

class TimeTable:
  def __init__(self, lines):
    self.routes = []
    self.stations = []
    self.nextStations = {}
    fields = []
    for l in lines[1:]:
      fields.append(l.split(","))
      self.stations.append(fields[-1][0])
    for r in range(1, len(fields[0])):
      route = []
      for s in range(len(fields)):
        station = fields[s][0]
        time = fields[s][r]
        if time != "":
          h, m = time.split(":")
          route.append((station, int(h)*60 + int(m)))
      self.routes.append(route)
    for ri in range(len(self.routes)):
      s, t = self.routes[ri][0]
      self.nextStations[(ri, None)] = (s, t)
      for ns, nt in self.routes[ri][1:]:
        self.nextStations[(ri, s)] = (ns, nt-t)
        s, t = ns, nt
      self.nextStations[(ri, s)] = (None, None)
  def __repr__(self):
    s = f"stations: {self.stations}\n"
    for ri in range(len(self.routes)):
      s += f"{ri}: {self.routes[ri]}\n"
    for k,v in self.nextStations.items():
      s += f"{k}: {v}\n"
    return s
  def nextStation(self, route, startStation):
    return self.nextStations[(route, startStation)]
  def allRoutes(self):
    return range(len(self.routes))
  def allStations(self):
    for s in self.stations:
      yield s

class States:
  start     = 0
  enroute   = 1
  inQueue   = 2
  atStation = 3
  done      = 4
  strings   = ('start', 'enroute', 'inQueue', 'atStation', 'done')
  @classmethod
  def toStr(cls, v):
    return cls.strings[v]

class Queue:
  def __init__(self):
    self.queue = []
  def __repr__(self):
    return f"{self.queue}"
  def add(self, route):
    for i,r in enumerate(self.queue):
      if route.srcStation == None and r.srcStation != None:
        self.queue.insert(i, route)
        return
      elif route.srcStation != None and r.srcStation != None and route.srcStation < r.srcStation:
        self.queue.insert(i, route)
        return
      elif route.srcStation == r.srcStation:
        if route.dstTime < r.dstTime:
          self.queue.insert(i, route)
          return
        elif route.dstTime == r.dstTime:
          if route.id < r.id:
            self.queue.insert(i, route)
            return
    self.queue.append(route)
  def size(self):
    return len(self.queue)
  def popFirst(self):
    if len(self.queue) > 0:
      return self.queue.pop(0)
    else:
      return None
  def check(self, timeTable):
    # Check that the srcStations are in order and that src->dst exist in the timetable
    maxSrc = None
    for r in self.queue:
      ns, nt = timeTable.nextStation(r.id, r.srcStation)
      if ns != r.dstStation:
        return False
      if r.srcStation == None and maxSrc != None:
        return False
      elif r.srcStation != None and maxSrc == None:
        maxSrc = r.srcStation
      elif r.srcStation != None and maxSrc != None:
        if r.srcStation < maxSrc:
          return False
        maxSrc = r.srcStation
    return True

class Route:
  def __init__(self, id, timeTable):
    self.id = id
    self.state = States.start
    self.srcStation = None
    self.dstStation, self.dstTime = timeTable.nextStation(id, None)
  def __repr__(self):
    return f"(id: {self.id+1} {self.srcStation} -> {self.dstStation})"
  def update(self, t, stations, timeTable):
#    print(f"id: {self.id}, state: {States.toStr(self.state)}")
    if self.state == States.start or self.state == States.enroute:
      if t == self.dstTime:
        if self.state == States.start:
          self.startTime = t
        q = stations[self.dstStation].queue
        q.add(self)
#        if self.srcStation == None:
#          print(f"Queue for {self.dstStation}: {q.queue}") 
        if not q.check(timeTable):
          print(f"ERROR: {q.queue}") 
        self.state = States.inQueue
        print(f"{t:5}: {self.id+1} enters queue for {self.dstStation}")
    elif self.state == States.atStation:
      if t == self.departureTime:
        if self.dstStation == None:
          self.state = States.done
          self.endTime = t
        else:
          self.state = States.enroute
        stations[self.srcStation].route = None
        print(f"{t:5}: {self.id+1} leaves station {self.srcStation}")

class Station:
  def __init__(self):
    self.route = None
    self.queue = Queue()
  def update(self, t, timeTable):
    if self.route == None:
      r = self.queue.popFirst()
      if r != None:
        self.route = r
        r.state = States.atStation
        r.departureTime = t + 5
        ns, nt = timeTable.nextStation(r.id, r.dstStation)
        r.srcStation = r.dstStation
        r.dstStation = ns
        if nt != None:
          r.dstTime = r.departureTime + nt
        print(f"{t:5}: {r.id+1} enters station {r.srcStation}")

class State:
  def __init__(self, timeTable):
    self.timeTable = timeTable
    self.stations   = {s:Station() for s in timeTable.allStations()}
    self.routes     = [Route(i, timeTable) for i,_ in enumerate(timeTable.allRoutes())]
  def update(self, t):
    for r in self.routes:
      r.update(t, self.stations, self.timeTable)
    for s in self.stations.values():
      s.update(t, self.timeTable)
#    for k,v in self.stations.items():
#      if v.queue.size() > 0:
#        print(f"{k}: {v.queue}")
  def allDone(self):
    for r in self.routes:
      if r.state != States.done:
        return False
    return True
  def maxRouteTime(self):
    mt = 0
    mr = None
    for r in self.routes:
      t = r.endTime - r.startTime
      if t > mt:
        mt = t
        mr = r
    return (mr, mt)

def solve(lines):
  timeTable = TimeTable(lines)
#  print(timeTable)
  state = State(timeTable)
  t = 0
  while not state.allDone():
    state.update(t)
    t += 1
#  for r in state.routes:
#    print(f"id: {r.id+1:4}, startTime: {r.startTime:4}, endTime: {r.endTime:4}, travelTime: {r.endTime - r.startTime:4}")
  mr, mt = state.maxRouteTime()
#  print(f"Longest Route:: id: {mr.id+1}, startTime: {mr.startTime}, endTime: {mr.endTime}")
  print(f"Solution: {mt}")

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
