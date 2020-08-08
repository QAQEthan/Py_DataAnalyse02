import numpy as np

# 替换nan为平均值
def fill_ndarray(t1):
    for i in range(t1.shape[1]):  # 遍历每一列
        temp_i_t1 = t1[:, i]  # 取出第i列数据
        count_nan = np.count_nonzero(temp_i_t1[temp_i_t1 != temp_i_t1])  # 统计该列nan的个数
        if count_nan != 0:  # 说明该列有nan
            temp_not_nan_i = temp_i_t1[temp_i_t1 == temp_i_t1]  # 保存该列非nan的数据
            temp_mean = np.mean(temp_not_nan_i)  # 求该列平均值
            temp_i_t1[temp_i_t1 != temp_i_t1] = temp_mean
            pass
        pass
    return t1


t1 = np.arange(1, 13).reshape((3, 4)).astype(float)
t1[1, 2:] = np.nan
print(t1)

# 注意temp得到的实际上是地址，因次使用temp修改数据时，仍然是对原数组的修改
# print(id(t1[:, 0]))
# temp = t1[:, 0]
# print(id(temp))
# 拷贝要使用
# t2 = t1.copy()            # 这样才会开辟新的内存空间

t1 = fill_ndarray(t1)
print(t1)
