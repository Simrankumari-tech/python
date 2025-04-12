import pandas as pd
var = pd.DataFrame({"a":[1,2,3] , "b":[4,5,6]})
print(var)
var.insert(1,"py",[7,86,54])
print(var) 