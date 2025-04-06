class employee:
  name = "harry"
  lang = "py"
  salary =123456


  def get(self) :  print(f"the lan is {self.lang}. yhe salary is {self.salary}")

  def greet(self):
    print("goof") 


hi = employee()
hi.get()
hi.greet()