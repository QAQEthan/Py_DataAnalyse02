import numpy as np

print(np.nan == np.nan)

# 统计数组中不为0的个数
t1 = np.arange(1,25).reshape(4,6)
print(t1)
t1[:,0] = 0
print(t1)
print(np.count_nonzero(t1))

print('-*'*50)

t1 = t1.astype(float)
print(t1)
t1[[2,3],[3,4]] = np.nan
print(t1)
# 统计数组中有多少nan
print(np.count_nonzero(t1!=t1))
# 另个一种方式
print(np.count_nonzero(np.isnan(t1)))

# nan和任何数据做元素都是nan
print(np.sum(t1))
# 问题，如何给nan替换，使得不影响求均值或者中值

print(t1.sum(axis=0))

print('^-'*50)
# 求均值
print(np.mean(t1,axis=0))

# 求最值
print(np.max(t1,axis=0))
print((np.min(t1,axis=0)))

# t1没有median方法
# print(t1.median(axis=0))

print(np.median(t1,axis=0))

# 求极值之差
print(np.ptp(t1,axis=0))

# 求标准差
print(np.std(t1,axis=0))
