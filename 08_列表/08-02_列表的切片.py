# 切片
# 切片是指從現有列表中，獲取一個子列表
# 創建一個列表，一般創建一個列表時，變量的名字會使用複數
stus = ['孫悟空', '豬八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']

# 列表的索引可以是負數
# 如果索引是負數，則會從後向前獲取元素，-1表示倒數第一個，-2表示倒數第二個，依此類推
print(stus[-1])

# 通過切片來獲取指定的元素
# 語法: 列表[起始:結束(不包含)]
#       通過切片獲取元素時，會包含起始位置元素，但不包含結束位置元素
#       做切片操作時，總會返回一個新的列表，不會影響原來的列表
print(stus[0:2])
print(type(stus[0:1]) == str)
#       如果省略結束位置，則會一直擷取到最後
#       如果省略開始位置，則會從第一個位置開始擷取
#       *如果開始位置和結束位置都省略，相當於創建了一個列表的副本
print(stus[1:])

# 語法: 列表[起始:結束(不包含):步長]
# 步長表示，每次獲取元素的間隔，默認值為1
print(stus[0:5:2])

# 步長不能是0，但可以是負數
# print(stus[::0]) ValueError: slice step cannot be zero
print(stus[::-1])


# 實際應用案例little-endian <--> big-endian 轉換
data_in_little = '11223344'
data_in_big_bytearray = bytearray.fromhex(data_in_little)[::-1]
data_in_big_bytearray[0] = 0x11
print('type = %s , result = 0x%s' % (type(data_in_big_bytearray), data_in_big_bytearray.hex()))


data_in_little = '11223344'
data_in_big_bytearray = bytes.fromhex(data_in_little)[::-1]
# TypeError: 'bytes' object does not support item assignment
# data_in_big_bytearray[0] = 0x11
print(type(data_in_big_bytearray[0]))
print('type = %s , result = 0x%s' % (type(data_in_big_bytearray), data_in_big_bytearray.hex()))


"""
bytes和bytearray差異

1. bytes不可以更改元素內容，bytearray可以更改元素內容

常用方法
1. fromhex(data: str) 將一個16進字符串轉換為bytes/bytearray
2. hex() 將bytes/bytearray轉換為16進制數組

"""


# 列表的傳遞是透過指針
A = [1, 2, 3]
B = A
# 如果A,B要是不同對象可以使用copy()方法
# B = A.copy()

B[0] = 2
# 雖然變的是B但A也被改變了
print(f'A={A}')
print(f'B={B}')
print(f'ID A={id(A):#x}')
print(f'ID B={id(B):#x}')







