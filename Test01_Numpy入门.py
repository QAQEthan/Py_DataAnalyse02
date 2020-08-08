import numpy as np
import random

# 使用numpy生成数组
t1 = np.array([1,2,3,4])
print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)

t3 = np.arange(10)
print(t3)
print(t3.dtype)

t4 = np.arange(10,dtype='float32')
print(t4)
print(t4.dtype)

t5 = np.array([1.2,3.4,5.6],dtype='float32')
print(t5)
print(t5.dtype)

t6 = np.array([1,1,0,1,0,0,1],dtype='?')
print(t6)
print(t6.dtype)


# 修改原有的数据类型
t7 = t6.astype('int16')
print(t7)
print(t7.dtype)


# 保留两位小数
t8 = np.array(['%.2f'%random.random() for i in range(10)],dtype='float16')
print(t8)


t9 = np.array([random.random() for i in range(10)],dtype='float32')
print(t9)
# 保留两位小数
t9 = np.round(t9,2)
print(t9)