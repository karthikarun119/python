import numpy as np 
a = np.array([ [1,2,3],[4,5,6]]  ) 
print( a)
a.shape=(3,2)
print( a)
'''n=int(input())
print(n)
lis=[]
for i in range(n):
    a=raw_input() 
    lis.append(a)
print(lis)'''
t = "07:05:45PM"

hrs = int( t.split() )

if hrs > 12:
    t = t.replace( str(hrs), str(hrs+12) )
print(t)