import pandas as pd
var = pd.DataFrame({"a" :[1,2,3,4] , "b":[6,5,4,3]})
var["c"] = var["a"] + var["b"]
print(var)