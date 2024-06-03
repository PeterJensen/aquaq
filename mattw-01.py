class C:
  None

c = C()
c.x = 1
c.y = 2
C.mf = lambda self: self.x + self.y
c.sf = lambda a,b: a+b


print(c.mf())
