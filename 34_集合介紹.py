# 集合(set)
# 集合和列表非常相似
# 不同點:
#   1. 集合只能儲存不可變對象
#   2. 集合中儲存的對象是無序的(不是按照元素的插入順序保存)
#   3. 集合中不能出現重複的元素

# 集合
# 使用{}來創建集合
s = {1, 10, 3, 4, 5}
# s = {[1, 2, 3], [4, 5, 6]} TypeError: unhashable type: 'list'
print(s, type(s))

# 使用set()函數來創建集合
s = set()   # 創建空集合

# 可以通過set()來將序列和字典轉換為集合
s = set([1, 3, 5, 6, 7, 7, 8])
s = set('aadakjf;f')
s = set({'a': 1, 'b': 2, 'c': 3})
print(s)

# 使用in和not in來檢查集合中元素
print('c' in s)

# 使用len()來獲取集合中的元素數量
# add()向集合中添加元素
s.add('f')
print(s)

# update() 將一個集合中的元素，添加到當前集合中
# update()可以傳遞序列和字典作為參數，字典只會使用鍵
s1 = set('abc')
# s2 = set('dfg')
s2 = set((10, 20, 30, 40, 50))
s1.update(s2)
print(s1)
# {'a', 'c', 40, 10, 50, 'b', 20, 30}
# pop() 隨機刪除集合中的一個元素並返回刪除元素
print('s1=', s1, 'del=', s1.pop())

# remove() 刪除集合中的指定元素
# 元素不存在會報錯 KeyError: '100'
tmp = s1.remove('100')
print(s1, tmp)

# clear() 清空集合
s1.clear()

# copy() 對集合進行淺複製


