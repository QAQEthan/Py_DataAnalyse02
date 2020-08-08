import numpy as np

# argmin(),argmax()求最小最大值的位置
t = np.eye(6)
print(t)
# print(np.argmax(t,axis=0))
# print(np.argmin(t,axis=0))          # 找出第一个最小值

# 生成随机数组
# t = np.random.random((3,4))         # 生成shape(3,4)的取值在0--1之间的浮点数
# t = np.random.randint(1,6,(4,5))      # 生成1--6之间（包括1不包括6）的shape(4,5)的矩阵
t = np.random.rand(5)                 # 均匀分布
# t = np.random.randn(5)                # 正态分布
print(t)

# 随机数种子
np.random.seed(5)       # 无论什么时候用，只要种子号是5，都是那几个数
# np.random.seed(4)
t = np.random.randint(5,9,(2,4))
print(t)
