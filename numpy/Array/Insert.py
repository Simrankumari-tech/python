import numpy as np
arr = np.array([10,20,30,40,50])
print(arr)

new_arr = np.insert(arr,2,100)
print(new_arr)



import numpy as np
arr_2d = np.array([[1,2] , [3,4]])
print(arr_2d)
new_arr_2d = np.insert(arr_2d,1,[5,6],axis=0)
print(new_arr_2d)