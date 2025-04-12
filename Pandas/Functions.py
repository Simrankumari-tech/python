 import pandas as pd
import numpy as np
csv_1 = pd.read_csv(r"C:\Users\simra.ANKIT-PC\OneDrive\Desktop\python\Pandas\sales_data_sample.csv",encoding="latin1")

#  1.   print(csv_1.index)  output=RangeIndex(start=0, stop=2823, step=1)

#  2.   print(csv_1.columns) sare column k nam d dega

#  3.   print(csv_1.describe()) sbke min , max,count,std,25%, 75% sb ah jayega

#  4.   print(csv_1.head())  starting k 5 ah jayega

#  5.   print(csv_1.tail()) last k dikh jayega

#  6.   print(csv_1[6:10])   itne range k data mil jayegaaa

#  7.   print(csv_1.index.array) array m change ho jayegaa
 
#  8. case-1  print(csv_1.to_numpy())  isse sara data array m ah jayega with all row,col

#  9. case-2      v = np.asarray(csv_1)
#                 print(v)

# 10.   print(csv_1.sort_index(axis=0, ascending=False)) //descending order m kr dega


# 11.   csv_1.loc[0,"ORDERNUMBER"] = 764932.0  agar value chnge krna ho to
#          print(csv_1)

# 12.    print(csv_1.loc[[1,2],["ORDERNUMBER" ,"DEALSIZE"]])


# 13.      print(csv_1.iloc[0,1]) 0:row ,1:col bs yhi one word m print krega not anything else

#14.   print(csv_1.drop("ORDERNUMBER" ,axis=1)) y wala show ni karegaa 
