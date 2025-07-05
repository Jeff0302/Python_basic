# 元組
# 元組是一個不可變的序列
# 它的操作方式基本上和列表一致
# 所以在操作元組時，就把元組當成一個不可變的列表
# 一般當我們希望數據不改變時，就使用元組，其餘情況都使用列表

# 創建元組
# 使用()來創建元組
t = ()  # 創建一個空元組
print(type(t))

my_tuple = (1, 2, 3, 4, 5)  # 創建一個五個元素的元組
print(my_tuple)
print(my_tuple[3])
# 元組是不可變對象，不能嘗試對元組中的元素重新賦值
# my_tuple[3] = 1  TypeError: 'tuple' object does not support item assignment

# 當元組不是空元組時，括號可以省略
# 如果元組不是空元組，它裡邊至少要一個逗號,
my_tuple = 1, 2, 3, 4, 5
my_tuple = 10,
print(my_tuple)

my_tuple = (10, 20, 30, 40)
a, b, c, d = my_tuple
print('a=', a)
print('b=', b)
print('c=', c)
print('d=', d)

# 在對元組進行解包時，變量的數量需要和元組中的元素數量一致
# 也可以在變量前面加一個*，這樣變量將會獲取元組中剩餘的所有元素
# a, b = my_tuple # ValueError: too many values to unpack (expected 2)
a, b, *c = my_tuple
print('c = ', c)
a, *b, c = my_tuple
print('b = ', b)

# 交換a和b的值，這時我們就可以利用元組的解包
a = 100
b = 300
a, b = b, a
print('a=', a)
print('b=', b)

# 常用16進操作
A = '0022FF'

#A_byte = [A[i:i+2] for i in range(0, len(A), 2)][-1::-1]
A = bytes.fromhex(A)[::-1]
print(A.hex())
