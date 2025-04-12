import pandas as pd
d = {"a":[1,2,3,4] , "s":[5,6,7,8]}
var  = pd.DataFrame(d)
print(var["a"][3])