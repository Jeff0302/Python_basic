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

########################################################################################################################
# 方法2
# 在創建字符串時，可以在字符串中指定佔位符
"""
1. 佔位符
    %s 在字符串中表示任意字符串
    %d 整數佔位符
    %f 符點數佔位符
    %x/%X 無符號整數的16進制表示
    %o 無符號的八進制表示

2. 指定精度及寬度
    指定寬度和精度
    格式控制的語法結構：
    %[flags][width][.precision]type
    
    flag 
    1. - : 左對齊(默認都是右對齊)
    2. + : 顯示正負號
    3. 空格: 表示在正數前預留一個空白位置。這有助於整齊對齊帶符號和不帶符號的數據
    4. 0 :　數字補零
    
3. 使用字典進行格式化命名
    '%(key)type' % dict  
    
4. 多個參數時，必須使用元組將所有變量包含進去

"""

# 打印16進制
num = 255
print('%#x' % num)

b = "Welcome python"
# 默認右對齊
print('----% 30s-----' % b)
# 設置左對齊
print('----%-30s-----' % b)

# 小數精度，正號留空格
f_number = 23.111111111
print('%+.4f' % f_number)
print('% .4f' % f_number)

# 正號留空,小數兩位,寬度7
f_number = 23.1144
print('% 7.2f' % f_number)


# 使用字典進行命名格式化
person = {'name': 'jeff', 'age': 18}
print('我是%(name)s, 今年%(age) d歲' % person)

# 多個參數使用元組
b = 'hello %s 你好 %s ' % ('jeff', 'amy')

########################################################################################################################
# 方法3
"""
  使用format方法
  1. 使用位置參數
    'a = {}, b = {}'.format(a, b)
     也可以指定位置
    'b = {1}, a = {0}'.format(a, b)
    
  2. 使用關鍵數參數
    'key1 = {key1}, key2 = {key2}. format(key1='value1', key2='value2')

  3. format() 方法允許在大括號內添加格式規範
     'a = {:[填充符號][對齊][width][.precision]type}'.format(a)

    填充符號: 寬度 < 指定寬度(width)時的填充符號
    對齊: > 右對齊 , < 左對齊,  ^置中對齊  
    width: 指定寬度
    .precision: 指定精度
    type: s, d, f, x/X, o
"""

a = 10
b = 20
# 默認index由小到大依序填充
# 也可以指定位置
print( 'a = {}, b = {}'.format(a, b))
print( 'b = {1}, a = {0}'.format(a, b))

# 使用關鍵字參數
print('name= {name}, age = {age}'.format(name='Jeff', age=22))
person = {'name': 'Jeff', 'age': 25}
print('name= {name}, age = {age}'.format(**person))

# 使用format方法，輸出16進制
num = 160
print('0x{:0>8x}'.format(num))
print('{:#010x}'.format(num))


num = 160.222
print('{:08.2f}'.format(num))
print('{:-^12.2f}'.format(num))

# 使用format方法，輸出------xxx------
title = 'Welcome Test System'
print('{:-^50s}'.format(title))

########################################################################################################################
# 方法4
# 格式化字符串，可以通過在字符串前添加一個f創建一個格式化字符串
# 在格式化字符串中可以直接嵌入變量
"""
    f'變量: [填充符號][對齊][width][.precision]type'
    
    填充符號: 寬度 < 指定寬度(width)時的填充符號
    對齊: > 右對齊 , < 左對齊,  ^置中對齊  
    width: 指定寬度
    .precision: 指定精度
    type: s, d, f, x/X, o

"""
name = 'Alice'
age = 30.11
print(f'我是{name}, 今年{age:-^10.2f}歲')

# 字符串的複製
# *在語言中表示乘法
# 如果將字符串和數字相乘，則解釋器會將字符串重複定次數並返回
d = '123'
d = d*10
print(d)