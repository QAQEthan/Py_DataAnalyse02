import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 设置自己的字体
myfont = font_manager.FontProperties(fname='C:\WINDOWS\FONTS\SIMSUN.TTC')

# 绘制评论数量直方图
us_file_path = './youtube_video_data/US_video_data_numbers.csv'
uk_file_path = './youtube_video_data/GB_video_data_numbers.csv'

# 读取数据
t1 = np.loadtxt(us_file_path,delimiter=',',dtype=int)       # 读取数据
comment = t1[:, -1]
# 剪枝操作
comment = comment.clip(0, 5000)
# print(max(comment)-min(comment))
# 绘制直方图,发现数据都集中在5000以内

# 绘制画布
plt.figure(figsize=(20,8))

# 画直方图
plt.hist(comment,50)

# 绘制x轴坐标信息
x = range(5001)
plt.xticks(x[::100],rotation=45)

# 设置标题，x,y轴描述
plt.title('电影评论直方图',fontproperties=myfont,size=16)
plt.xlabel('评论数（条）',fontproperties=myfont,size=16)
plt.ylabel('电影数（部）',fontproperties=myfont,size=16)

# 展示
plt.show()