import pandas as pd
var = pd.DataFrame({"a":[1,2,4,6] , "b":[7,8,9,2]})

var1 =var.pop('b')
print(var1)
print(var)