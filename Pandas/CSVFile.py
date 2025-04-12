import pandas as pd
dis={"a":[1,2,3,4] , "b":[4,5,6,7] , "c":[8,9,7,6]}
d = pd.DataFrame(dis)
d.to_csv("test_new.csv",index=False,header=[1,2,3])
print(d)
