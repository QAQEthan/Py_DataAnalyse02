import numpy as np

t1 = np.array(range(1,25)).reshape((4,6))
print(t1)
print(t1<10)
t1[t1<10] = 3
print(t1)

# 修改
t1 = np.where(t1<10,0,10)
print(t1)

t1 = t1.clip(10,20)
print(t1)

t1 = t1.astype(float)
print(t1)
t1[0][0] = np.nan
print(t1)