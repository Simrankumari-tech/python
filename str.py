class comple:
  def __init__(self,r,i):
    self.r = r
    self.i = i


  def __add__ (self, c2):
      return comple(self.r +c2.r , self.i+ c2.i)
    
  def __str__(self):
      return f"{self.r}  + {self.i}i"


c1= comple(1,3)
c2= comple(7,8)
print(c1+c2)    

