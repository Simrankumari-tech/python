import pandas as pd
sr = {"s" : pd.Series([1,2,3,4,5]) , "r": pd.Series([6,7,8,9,1])}
var3 = pd.DataFrame(sr)
print(var3)