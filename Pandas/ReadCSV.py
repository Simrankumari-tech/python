import pandas as pd
# df = pd.read_csv(r"C:\Users\simra.ANKIT-PC\OneDrive\Desktop\python\Pandas\sales_data_sample.csv", nrows=10,encoding='latin1' , usecols=[0,2],skiprows=[0,1])


# df = pd.read_csv(r"C:\Users\simra.ANKIT-PC\OneDrive\Desktop\python\Pandas\sales_data_sample.csv", nrows=10,encoding='latin1',index_col="DEALSIZE")


# df = pd.read_csv(r"C:\Users\simra.ANKIT-PC\OneDrive\Desktop\python\Pandas\sales_data_sample.csv", nrows=10,encoding='latin1',header =2) 




# heading chnge krna chahe 
# df = pd.read_csv(r"C:\Users\simra.ANKIT-PC\OneDrive\Desktop\python\Pandas\sales_data_sample.csv", nrows=10,encoding='latin1',names=["col1" , "col2" , "col3" , "col4" , "col5"])




# convert in float
df = pd.read_csv(r"C:\Users\simra.ANKIT-PC\OneDrive\Desktop\python\Pandas\sales_data_sample.csv", nrows=10,encoding='latin1',dtype={"ORDERNUMBER" : "float"})

print(df)
