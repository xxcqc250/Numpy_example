import numpy as np

#如果print的東西太多，他會省略
print("如果print的東西太多，會省略如下")
print("EX1:\n",np.arange(10000),"\n")
#輸出變這樣
# [   0    1    2 ..., 9997 9998 9999]
print("EX2:\n",np.arange(10000).reshape(100,100))

#如果要取消省略的話，須設定如下
# np.set_printoptions(threshold='nan')
print(np.arange(100))
