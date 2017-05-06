import numpy as np
#建立一維array
a=np.array([2,3,4]) #引用Numpy的array，而不是python的array
print("a:")
print(a)
print(a.dtype)
b=np.array([1.,3.,5.])
print("b:")
print(b)
print(b.dtype)

#建立二維array
a=np.array([[1,2,3],[4,5,6]],dtype=np.int64) #可以直接指定dtype
print("\nTwo Dimentional\n a:")
print(a)
print("dimention is :",a.ndim)
print("dtype is : ",a.dtype)

#建立零矩陣
zero_array=np.zeros((3,4),dtype=np.float64)
print("\nThe zero array:")
print(zero_array)

np_empty=np.empty((2,3))
print(np_empty,"\n")

#linspace範例
from numpy import pi
num_space= np.linspace(0,2,9) #從0到2中列出9個數字(等距離)(=8個間隔)
print("np.linspace:")
print(num_space)

#還不知道功用是甚麼，但是他說"好用在很多點的運算時"
x=np.linspace(0,2*pi,100)
f=np.sin(x)
print(f)



