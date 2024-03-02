# 關係運算符
"""
    關係運算符用來比較兩個值之間的關係，會返回一個布爾值
    如果關係成立返回True，反則返回False
    >        比較左側值是否大於右側值
    >=       比較左側值是否大於等於右側值
    <        比較左側值是否小於右側值
    <=       比較左側值是否小於等於右側值

    ==       比較兩個對象的值是否相等
    !=       比較兩個對象的值是否不相等
    --> 相等和不相等比較的是對象的值，而不是id

    is       比較兩個對象的是否是同一個對象
    is not   比較兩個對象的是否不是同一個對象
    --> 比較的是對象的id

"""
result = 10 > 20    # False
result = 30 > 20    # True
result = 30 < 20    # False
result = 10 > 10    # True

result = 2 > True   # True
print('result= ', result)

# 在Python中可以對兩個字串進行大於(等於)或小於(等於)的運算
# 當對字符串進行比較時，實際上比較的是字符串的Unicode編碼
# 比較兩個字串的Unicode編碼時，是逐位比較的
# 利用此特性可以讓字符串按照字母順序進行排序

result = '2' > ' 1'   # True
result = '2' > ' 11'  # True
result = 'a' > 'b'  # False
result = 'ab' > 'b'  # False
result = 'ab' > 'ab'  # False
print('result= ', result)

result = 1 == 1                 # True
result = 'hello' == 'hello'     # True
result = 'abc' == 'bcd'         # False
result = 'abc' != 'bcd'         # True
result = 1 == True              # True
a = 1
result = a is True              # False

print('result= ', result)
print(id(1), id(True))
