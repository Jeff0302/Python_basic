# 創建一個列表
stus = ['孫悟空', '豬八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']

# + 和 *
# +可以將兩個列表拼接為一個列表
my_list = [1, 2, 3] + [4, 5, 6]
print(my_list)

# *可以將列表重複一個指定的次數
my_list = [1, 2, 3] * 5
print(my_list)

# in 和 not in
# in用來檢查指定元素是否存在列表內，如果存在返回True，否則返回False
# not in用來檢查指定元素是否不存在列表內，如果不存在返回True，否則返回False
print('孫悟空' in stus)

# len()獲取列表中元素的個數

# min() 獲取列表中的最小值
# max() 獲取列表中的最大值
arr = [10, 1, 2, 5, 100, 77, 100]
print('max = ', max(arr), ',min=', min(arr))

# 兩個方法(method)，方法和函數基本上是一樣的，只不過方法必須通過  對象.方法() 的形式調用

# index() 返回列表中指定元素的索引，如果有多個相同元素，則會返回第一個索引
#         如果指定元素不存在會拋出異常 ValueError: 200 is not in list
# print(arr.index(200))
# index()的第二個參數，表示查找的起始位置，第三個參數，表示查找的結束位置(不包含)
print(arr.index(10, 3))
print(arr.index(10, 3, 5))

# count() 返回列表中指定元素的個數，元素不存在，則返回0
print(arr.count(100))