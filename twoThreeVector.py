class twoVector:
  def __init__(self,i,j):
   self.i = i 
   self.j = j
  
  def show(self):
    print(f"the vector is {self.i}i + {self.j}j")

class three(twoVector):
  def __init__(self , i, j,k):
    super().__init__(i,j)
    self.k = k

  def show(self):
    print(f"the vector is {self.i}i +{self.j}j + {self.k}k")



a = twoVector(1,4)
a.show()

b = three(5,7,5)
b.show()
   