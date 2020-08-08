import numpy as np

# t1 = np.arange(1,21).reshape((4,5))
# t2 = np.arange(21,37).reshape((4,4))

# 水平拼接,注意传入参数是元组
# t3 = np.hstack((t1,t2))
# print(t3)

# 交换行,实际上就是赋值操作
# t3[2:,:] = t3[1:,:] # 报错，不能把could not broadcast input array from shape (3,9) into shape (2,9)
# t3[[1,2],:] = t3[[2,1],:]
# print(t3)

us_path = './youtube_video_data/US_video_data_numbers.csv'
uk_path = './youtube_video_data/GB_video_data_numbers.csv'

# 读取数据
us_data = np.loadtxt(us_path,delimiter=',',dtype=int)
uk_data = np.loadtxt(uk_path,delimiter=',',dtype=int)

# 创建全0数据
us_mark = np.zeros((us_data.shape[0],1),dtype=int)
uk_mark = np.ones((uk_data.shape[0],1),dtype=int)

# 水平拼接数据
us_data = np.hstack((us_data,us_mark))
uk_data = np.hstack((uk_data,uk_mark))

# 竖直拼接数据
final_data = np.vstack((us_data,uk_data))

print(final_data)


