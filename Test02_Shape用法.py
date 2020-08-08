import numpy as np
import numpy.linalg as la
import random

t1 = np.array(range(12))
print(t1)
print(t1.shape)

t2 = np.array([[1,2,3],[4,5,6]])
print(t2)
print(t2.shape)

t3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(t3)
print(str(t3.shape)+'hahaha')

t4 = np.array(range(24))
t4 = t4.reshape((3,2,4))
print(t4)

t5 = t4.reshape((t4.shape[0]*t4.shape[1]),t4.shape[2])
print(t5)

t6 = t5.flatten()
print(t6)

t7 = t5+3
print(t7)

print(t6*2)

print(t6/0)

print('-*'*50)

t8 = np.array(range(50,74)).reshape((6,4))
print(t8+t5)

print('-$'*50)
t9 = np.array(range(0,4))
print(t8-t9)

t10 = np.array(range(6)).reshape((6,1))
print(t8)
print(t8-t10)


# shape(3,3,2) 和 shape(3,3)不能运算
# t11 = np.array(range(200,204)).reshape((2,2))
# print(t3-t11)

print('@-'*50)
t11 = np.array(range(1,26)).reshape((5,5))
print(t11)
# 输出相关系数矩阵
print(np.corrcoef(t11))
# 输出上三角矩阵       下三角矩阵使用tril
print(np.triu(t11))
# 矩阵对角线
print(np.diag(t11))
# 矩阵的转置
print(np.transpose(t11))
# 计算矩阵的迹
print(np.trace(t11))

# repeat()方法创建矩阵
t12 = np.repeat(3,4)
print(t12)

print('--等差--'*25)
# linspace()产生等差数列
t13 = np.linspace(1,9,5)        # 产生从1--9共5个数字的等差数列
print(t13)

# 求矩阵的行列式
print('--方阵--'*25)
t14 = np.array([random.randint(1,5) for i in range(16)]).reshape((4,4))
print(t14)
print(la.det(t14))

# 求逆矩阵
print(la.inv(t14))

# 特征值的分解
print(la.eig(t14))

# 奇异值的分解
print(la.svd(t14))

# 数组求和
print(t14.sum())
# 按列求和
print(t14.sum(axis=0))
# 按行求和
print(t14.sum(axis=1))

# 数组求乘积
print(t14.prod())
# 按列求乘积
print(t14.prod(axis=0))
# 按行求乘积
print(t14.prod(axis=1))

# max(),min()求最大最小值、
# 默认对整个数组求最值
# 设置axis属性为0时，对列求最值
# axis为1时，对行求最值

# 求方差var和标准差std
print(t14.var())
print(t14.var(axis=0))
print(t14.var(axis=1))
print(t14.std())
print(t14.std(axis=0))
print(t14.std(axis=1))

# 求平均数
print(t14.mean())

# 对数组每个元素开方
print(np.sqrt(t14))

# 对每个元素求平方
print(np.square(t14))

# 以e为底的指数次方
print(np.exp(t14))

# 计算每个元素的对数
print(np.log10(t14))

print(t8@t14)