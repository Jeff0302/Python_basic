# 格式化字符串
a = 'hello'

# 字符串之間也可以進行加法運算
# 如果將兩個字符串進行相加，則會自動將兩個字符串拼接為一個
a = 'Hello ' + 'world'
# 這種寫法在Python中不常見
"""
    字符串不能和其他類型進行加法運算，如果做了會出現錯誤
    TypeError: can only concatenate str (not "int") to str
"""
a = 123
# 方法1
# print('a=', a)

# 方法2
# 在創建字符串時，可以在字符串中指定佔位符
"""
    %s 在字符串中表示任意字符串
    %f 符點數佔位符
    %d 整數佔位符
"""
# b = 'a= %d'
b = 'hello %s 你好 %s ' % ('jeff', 'amy')
b = 'hello %3s' % 'ab'
# %3.5s字符串長度限制在3-5之間
b = 'hello %3.5s' % 'abcdefg'

b = 'hello %.2f' % 123.1111
b = 'hello %d' % 123.1111
print(b)

# 方法3
# 格式化字符串，可以通過在字符串前添加一個f創建一個格式化字符串
# 在格式化字符串中可以直接嵌入變量
c_sub = 'world'
c = f'hello {c_sub}'
print(c)

# 字符串的複製
# *在語言中表示乘法
# 如果將字符串和數字相乘，則解釋器會將字符串重複定次數並返回
d = '123'
d = d*10
print(d)