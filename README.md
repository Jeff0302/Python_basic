

[TOC]

# 1. 變量

## 1-1. 創建變量 - `變量名 = 變量值`

>1. Python中使用變量，不需要聲明，直接為變量賦值即可。
>2. 不能使用沒有賦值過的變量，如果使用沒有賦值過的變量會報錯。
>3. Python是一個動態類型語言，可以為變量賦值任意類型的值，也可以任意修改變量的值。



## 1-2. 變量的標誌符 - `可以自主命名的內容都屬於標誌符`

### 1-2-1. 下劃線命名法

### 1-2-2. 大駝峰命名法

+  在Python中所有可以自主命名的內容都屬於標誌符，比如: 變量名、函數名、類名。

> 標誌符必須遵守標誌符規範
>
> 1. 標誌符中可以含有字母、數字、_，但不能用數字開頭
>
> 2. 標誌符不能是Python中的關鍵字和保留字，，也不建議使用Python中的函數名作為標字符，因為這樣會導致函數被覆蓋。
>
> 3. 命名規範: 在Python中注意遵守兩種命名規範
>     
>     - `下劃線命名法`: 
>         所有字母小寫，單詞之間使用_分割 `max_length`                
>     
>     - ` 帕斯卡命名法`(大駝峰命名法):
>       首字母大寫,每個單詞開頭字母大寫,其餘字母小寫 `MaxLength`
>     
>\* 如果使用不符合標準的標誌符，將會報錯 `SyntaxError: invalid syntax`
>
> 

# 2.數據類型(變量值讀類型)

## 2-1. 數值

### 2-1-1. 整數 `int`

>1. 在Python中所有正數都是int類型
>2. 在Python中整數的大小沒有限制，可以是一個無限大的整數
>3. 如果數字長度過大，可以用下劃線作為分隔符

### 2-1-2. 浮點數 `float`

>1. 在Python中所有小數都是float類型
>2. 對符點數進行運算時，可能得到一個不精確的結果

```python
# 在Python中數值分成三種: 整數、符點數(小數)、複數
# 在Python中所有正數都是int類型
a = 10
print(type(a))
# 在Python中整數的大小沒有限制，可以是一個無限大的整數
b = 1111111111111111111111111111111111111111
print(b)

# 如果數字長度過大，可以用下劃線作為分隔符
c = 111_111_111
print(c)

# 其他進制的整數
# d = 0123 10進制數字不能0開頭
# 只要是數字打印時，一定是以10進制形式顯示
"""
   二進制  0b開頭 
   八進制  0o開頭
   十六進制 0x開頭
"""
c = 0b10
c = 0o10
c = 0x10
print(c)

# 也可以通過運算符來對數字進行運算
d = 100
d = d + 1
# d += 1
print(d)

# 符點數(小數), 在Python中所有小數都是float類型
e = 1.23
print(e)

# 對符點數進行運算時，可能得到一個不精確的結果
f = 0.1 + 0.2  # 0.30000000000000004
print(f)
```



## 2-2. 布爾值 `bool`及空值 `none`

### 2-2-1. 布爾值`bool`: 用來做邏輯判斷

### 2-2-2. 空值`none`: 用來表示不存在

```python
# 布爾值(bool)
# 布爾值主要用來做邏輯判斷
# 布爾值一共有兩個 True 和 False

a = True
a = False
print('a', a)

# 布爾值實際上也屬於整型, True相當於1, False相當於2
# print(1+True)

# None(空值)
# None專門用來表示不存在
b = None
print(b)

```



# 3. 字符串

## 3-1. 創建短字符串 - `'字符串'` `"字符串"` 

+ 引號可以是雙引號,也可以是單引號,但注意不要混著用。
+  相同引號之間不能嵌套。

## 3-2. 創建長字符串 

### 3-2-1.  `'字符串'\`

```python
# 長字符串
s = '1111111111'\
    '2222222222'\
    '3333333333'
```

### 3-2-2.  `'''字符串'''`

```  python
s = '''123
456
789
'''
```

## 3-3. 轉義字符 - `\`

+  可以使用\作為轉義字符，通過轉義字符，可以在字符中使用一些特殊內容。

>`\'` : 表示'
>
>`\"`: 表示"
>
>` \t`: 表示制表符
>
>` \n`: 表示表示換行
>
>` \`: 表示\
>
>`\u0000`: 表示Unicode編碼



## 3-4. 格式化字符串 - `%s`, `%d`, `%f`, `%x/%X`, `%o`

>`%s`: 在字符串中表示任意字符串
>
>`%d`: 整數佔位符 
>
>`%f`: 符點數佔位符
>
>`%x/%X`:  無符號整數的16進制表示
>
>`%o`:  無符號的八進制表示

### 3-4-1. 指定精度和寬度 - `%[flag][width][.precision]type`

### 3-4-2. flag說明

>`-`: 左對齊(默認都是右對齊)
>
>`+`: 顯示正負號
>
>`空格`: 表示在正數前預留一個空白位置。這有助於整齊對齊帶符號和不帶符號的數據
>
>`0` :　數字補零

### 3-4-3. 使用字典格式化命名  - `'%(key)type' % dict `

### 3-4-4. 多參數配合元組使用

```python
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

```



## 3-5. format使用`str.format()`

### 3-5-1. 使用位置參數 - `'a = {}, b = {}'.format(a, b)`

```python
a = 10
b = 20
# 默認index由小到大依序填充
# 也可以指定位置
print( 'a = {}, b = {}'.format(a, b))
print( 'b = {1}, a = {0}'.format(a, b))

```



### 3-5-2. 使用關鍵數參數 - `'key1 = {key1}, key2 = {key2}. format(key1='value1', key2='value2')`

```python
# 使用關鍵字參數
print('name= {name}, age = {age}'.format(name='Jeff', age=22))
person = {'name': 'Jeff', 'age': 25}
print('name= {name}, age = {age}'.format(**person))

```



### 3-5-3. format添加格式規範 - `'a = {:[填充符號][對齊][width][.precision]type}'.format(a)`

>`填充符號`:  寬度 < 指定寬度(width)時的填充符號
>
>`對齊`: > 右對齊 , < 左對齊,  ^置中對齊 
>
>`width`: 指定寬度
>
>`precision`: 指定精度
>
>`type`: s, d, f, x/X, o



```python
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

```

## 3-6. f-string使用 - `f'變量名 = {變量:format_spec}'`

```python
name = 'Alice'
age = 30.11
print(f'我是{name}, 今年{age:-^10.2f}歲')

```



# 4. 類型轉換

## 類型檢查 - `type(變量)`

```python
print(type(1))      # <class 'int'>
print(type(1.5))    # <class 'float'>
print(type('123'))  # <class 'str'>
print(type(True))   # <class 'bool'>
print(type(None))   # <class 'NoneType'>
```

## 轉Int類型 - `int(變量, [base])`

```python
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
```

## 轉float類型 - `float(變量)`

```python
a = 1
a = float(a)
print('a= ', a) # 1.0
print('type= ', type(a))

```

## 轉str類型 - `str(變量)`

```python
a = 123
a = str(a) # '123'
print('a= ', a)
print('type= ', type(a))
```

## 轉bool類型 - `bool(變量)`

```python
a = ''
a = bool(a) # False
print('a= ', a)
print('type= ', type(a))
```

> 注意:
>
> ​	調用方法來將變量轉換類型，函數不會對原來的變量產生影響，它是`將對象轉換為指定類型並作為返回值返回`。因此如果希望修改原先變量，則需要重新賦值。



---

# 5. 算術運算符

### 加法運算 `+`

### 減法運算 `-`

### 乘法運算 `*`

### 除法運算 `/`

### 整除運算 `//`

### 冪運算 `**`

### 取模(餘)運算 `%`

```python
a = 10 + 5
a = 'hello' + ' ' + 'world'

a = 10 - 5 # 5
a = 10 - True # 1
a = a - 2 # 8

a = 5 * 5 # 25
a = 10 / 5 # 2.0
a = 10 / 3 # 3.333...
a = 10 // 3 # 3

a = 2 ** 2 # 4
a = 16 ** 0.5   # 求16的平方根, 4

a = 10 % 2     # 0
a = 10 % 4     # 2
print("a= ", a)
```



---



# 教學資源

https://www.youtube.com/watch?v=K2EZ-beTdGM&list=PLmOn9nNkQxJFGvtKd7PI7AhsYmY-6FrJs&index=100