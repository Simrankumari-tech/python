class Employee:
  salary = 234
  increment = 29
  @property
  def salaryafterincrement(self):
    return (self.salary + self.salary*(self.increment/100))
  


  @salaryafterincrement.setter
  def salaryafterincrement(self,salary):
    self.increment=((salary/self.salary)-1)*100


e = Employee()
e.salaryafterincrement= 289
print(e.increment)
