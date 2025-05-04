#   類型轉換四個函數 int() float() str() bool()
"""
    int() 可以用來將其他對象轉換為整型
    規則:
        布爾值: True -> 1, False -> 0
        浮點數: 直接取整數, 省略小數點後的內容
        字符串: 合法的整數字串，則直接轉換為對應的數字
               如果是不合法的整數字符串，則報錯
        對於其他不可以轉換為整型的對象，直接拋出異常ValueError

    float()和int()基本一致，不同的是它會將對象轉換為浮點數
    str()可以將對象轉換為字符串
    bool()可以將對象轉換為布爾值，任何對象都可以轉換為布爾值
    規則: 對於所有表示空性的對象都會轉為False，其餘轉換為True
        哪些表示空性0, '', none

"""


a = True

# 調用int()來將a轉換為整型
# int()函數不會對原來的變量產生影響，它是將對象轉換為指定類型並作為返回值返回
# 如果希望修改原來變量，則需要將變量重新賦值

a = int(a)
print('a= ', a) # 1
print('type= ', type(a))


a = int('123')
print('a= ', a) # 123
print('type= ', type(a))

a = int('100', 16)
print('a= ', a) # 256
print('type= ', type(a))

a = int(11.6)
print('a= ', a) # 11
print('type= ', type(a))


a = 1
a = float(a)
print('a= ', a) # 1.0
print('type= ', type(a))

a = 123
a = str(a) # '123'
print('a= ', a)
print('type= ', type(a))

a = ''
a = bool(a) # False
print('a= ', a)
print('type= ', type(a))
