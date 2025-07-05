# 列表的方法
import math

stus = ['孫悟空', '豬八戒', '沙和尚']
print('原列表:', stus)

# append()
# 向列表最後添加一個元素
stus.append('唐僧')   # 等同stus[len(stus):len(stus)] = ['唐僧']
print('新列表:', stus)

# insert()
# 向列表指定位置插入一個元素
# 參數:
#      1. 要插入的位置
#      2. 要插入的元素
stus = ['孫悟空', '豬八戒', '沙和尚']
stus.insert(1, '唐僧')
print('新列表:', stus)

# extend()
# 使用新序列來擴展當前序列
# 需要一個序列作為參數，它會將該序列中的元素添加到當前列表
stus = ['孫悟空', '豬八戒', '沙和尚']
stu2s = ['Jeff', 'Amy']
stus.extend(stu2s)      # stus += stu2s
# stus[3:3] = stu2s
print('新列表:', stus)

# clear() 清空序列
stus = ['孫悟空', '豬八戒', '沙和尚']
stus.clear()
print('新列表:', stus)

# pop()
# 根據索引刪除並返回被刪除元素
stus = ['孫悟空', '豬八戒', '沙和尚']
del_element = stus.pop(2)     # 刪除索引為2的元素
print('新列表:', stus, '被刪除元素:', del_element)

# remove()
# 刪除指定元素，如果相同值有多個，它只會刪除第一個
stus = ['孫悟空', '豬八戒', '沙和尚', '孫悟空']
stus.remove('孫悟空')
print('新列表:', stus)

# reverse() 反轉列表
stus = ['孫悟空', '豬八戒', '沙和尚']
stus.reverse()
print('新列表:', stus)

# sort()
# 用來對列表中元素進行排序，默認是升序排序
# 如果需要降序排列，則需要傳遞一個reverse=True作為參數
my_list = list('ahdksla')
print('修改前列表:', my_list)
my_list.sort(reverse=True)
print('修改後列表:', my_list)

# 對索引進行排序
b = list(range(4))
a = [10, 7, 8, 5]
b.sort(key=lambda x: a[x])
print(b)

