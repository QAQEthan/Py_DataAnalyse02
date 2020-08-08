import numpy as np


us_file_path = './youtube_video_data/US_video_data_numbers.csv'
uk_file_path = './youtube_video_data/GB_video_data_numbers.csv'

# 读取数据
t1 = np.loadtxt(us_file_path,delimiter=',',dtype=int)
t2 = np.loadtxt(us_file_path,delimiter=',',dtype=int,unpack=True)

print(t1)
print('-*'*50)
print(t2)
print(type(t2))
print('-&'*50)
print(t2.T)

# 要处理什么问题？
# 要用什么呈现方式
# 数据还需要做什么处理
# 编码

print('-取行-'*25)
# 取行
print(t1[2])

# 取多行
print(t1[3:])

# 取不连续的多行
print(t1[[2,3,10]])

# 列表测试
# t3 = [[1,2,3],[4,5,6]]
# print(t3[1][1:])

# 逗号前面是行的切片，逗号后面是列的切片
print('-切片-'*25)
print(t1[2:,1:])

# 只取一列时，会变成一维的数组
print(t1[:,0])
print(t1[:,0].shape)
# 一维数组的转置仍然是一维数组
# 转置有三个方法
# 1.t.T
# 2.t.swapaxes(0,1)
# 3.np.transpose(t)
print(t1[:,0].T)
print(t1[:,0].T.shape)

# 取多列时仍保持原来的shape
print(t1[:,[0,1]])
print(t1[:,[0,1]].shape)

# 取不相邻的点
# 取出来的值为[0,0],[1,1],[2,2]
print(t1[[0,1,2],[0,1,2]])