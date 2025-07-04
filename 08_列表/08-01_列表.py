"""
    列表(list)
    - 列表是Python中的一個對象
    - 對象(object)就是內存中專門用來儲存數據的一個區域
    - 之前學習的對象，像數值，它只能來保存一個單一的值
    - 列表中可以保存多個有序的數據
    - 列表的使用:
      1. 列表創建
      2. 操作列表中的數據
"""
# 創建列表，通過[]來創建列表
my_list = []
print(my_list, type(my_list))

# 列表中存儲的數據，我們稱為元素
# 一個列表中可以儲存多個元素，也可以在創建列表時，來指定列表中元素
my_list = [10]  # 創建一個只包含一個元素的列表

# 當向列表中添加多個元素時，多個元素之間使用，隔開
my_list = [10, 20, 30, 40, 50]  # 創建一個包含5個元素的列表
print(my_list)

# 列表中可以存儲任意數據類型
my_list = [10, '123', False, None, [1, 3, 3], print]

# 列表中的對象都會按照插入的順序儲存到列表中，第一個插入的對象保存到第一個位置
#                                   ，第二個插入的對象保存到第二個位置...
# 我們可以通過索引(index)來獲取列表中的元素，索引從0開始
my_list = [10, 20, 30, 40, 50]
print(my_list)

# 通過索引來獲取列表中的元素
print(my_list[4])
# 如果使用的索引超過最大範圍，會拋出異常。 IndexError: list index out of range
print(my_list[5])

# 獲取列表中的元素個數
# len()函數可以獲取列表的長度
# 獲取到的長度，是列表的最大索引+1
print(len(my_list))



