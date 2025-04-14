import pandas as pd
var1 =pd.DataFrame({"a":[1,2,3,4] , "b":[11,23,24,56]},index=["a","b","c","d"])
var2 =pd.DataFrame({"d":[18,24,37,48] , "c":[117,238,284,5866]})
print(var1.join(var2))