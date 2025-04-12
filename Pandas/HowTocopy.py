import pandas as pd
var = pd.DataFrame({"a":[1,2,3,4] , "b":[6,7,83,35]})
var["pthyon_12"] = var["b"][:3]
print(var)