# 通過類型檢查，可以檢查值(變量)的類型

a = 123     # 數值
b = '123'   # 字符串

# print('a=', a)
# print('b=', b)

# type() 用檢查值的類型
# 該函數會將檢查的結果作為返回值返回，可以通過變量來接收返回的結果
c = type(a)
c = type(b)
print(c)

print(type(1))      # <class 'int'>
print(type(1.5))    # <class 'float'>
print(type('123'))  # <class 'str'>
print(type(True))   # <class 'bool'>
print(type(None))   # <class 'NoneType'>



