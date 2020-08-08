import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager

# Test
# 4*6的矩阵
# t2 = np.arange(1,25).reshape((4,6))
# print(t2)
# # 通过筛选后变成一维的矩阵
# t2 = t2[t2<20]
# print(t2)

# 绘制评论数量直方图
us_file_path = './youtube_video_data/US_video_data_numbers.csv'
uk_file_path = './youtube_video_data/GB_video_data_numbers.csv'

# 读取数据，喜欢和评论
t1 = np.loadtxt(uk_file_path,delimiter=',',dtype=int)       # 读取数据
temp = t1[t1[:,1]<6e5]
like = temp[:,1]
comment = temp[:,3]

# 绘制画布
plt.figure(figsize=(20,8),dpi=80)

# 绘制点
plt.scatter(like,comment)

# 展示
plt.show()