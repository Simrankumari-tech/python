import numpy as np
arr1= np.array([1,23,45])
arr2 = np.array([23,45,78])
new_arr = np.concatenate((arr1,arr2))
print(new_arr)