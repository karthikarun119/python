import  numpy as np 
a=np.array( [[0,1,2,3,4],[2,3,4,5,6]] )
print(a)
import numpy as np 
b=[1, 2, 3,4,5]
a = np.array(b, ndmin = 3) 
print (a)
dt=np.dtype([('age',np.int32)])
a=np.array([1,2,3,4],dtype=dt)
print(a)