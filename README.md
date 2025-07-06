

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

<span alt="solid">範例: 01_變量</span>



---

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



<span alt="solid">範例: 02_數據類型</span>



---

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



<span alt="solid">範例: 03_字符串</span>



---

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



<span alt="solid">範例: 04_類型轉換</span>



---

# 5. 運算符

## 5-1. 算數運算符

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

## 5-2. 賦值運算符

### `+=` :  a += 5 相當於 a = a + 5

### `-=` :  a -= 5 相當於 a = a - 5

### `*=` :  a *= 5 相當於 a = a * 5

### `/=` :  a /= 5 相當於 a = a / 5

### `**=` :  a \*\*= 5 相當於 a =  a\*\* 5

### `//=` :  a //= 5 相當於 a = a // 5

### `%=` :  a %= 5 相當於 a = a % 5

```python
a = 10
a += 5
print('a= ',a) # 15
a -= 5
print('a= ',a) # 10
a **= 2
print('a= ',a) # 100
a /= 25
print('a= ',a) # 4.0
a = 25
a //= 5
print('a= ',a) # 5.0
a = 5
a %= 4
print('a= ',a) # 1
```



## 5-3. 關係運算符

### `>`: 比較左側值是否大於右側值 
### `>=`: 比較左側值是否大於等於右側值
### `<`: 比較左側值是否小於右側值 
### `<=`: 比較左側值是否小於等於右側值
### `==`: 比較左側值是否等於右側值
### `!=`: 比較左側值是否不等於右側值
### `is`: 比較兩個對象的是否是同一個對象
### `is not`: 比較兩個對象的是否不是同一個對象

```python
result = 10 > 20    # False
result = 30 > 20    # True
result = 30 < 20    # False
result = 10 > 10    # False

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
result = 'ac' > 'ab'  # False
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

```



## 5-4. 邏輯運算符

### 邏輯非`not`

>  not可以對符號右邊值進行非運算
>
>+ 對於布爾值，非運算會對其進行取反操作,True變False,False變True
>+ 對於非布爾值，非運算會先將其轉換為布爾值,然後再取反

```python
a = True
a = not a   # False
a = 1
a = not a   # False
```

### 邏輯與`and`

>  and可以將符號兩側的值進行與運算
>
>+ 只有在符號兩側值都回True時,才會返回True,只要有一個False則返回False
>+ 與運算是找False，`Python中的與運算是短路的與，如果第一個值是False,則不看第二個`

```python
result = True and True      # True
result = True and False     # False
result = False and True     # False
result = False and False    # False

False and print('你猜我出來出來嗎?') # print不會執行
True and print('你猜我出來出來嗎?')  # print會執行
```

### 邏輯或`or`

>  or可以對符號兩側的值進行或運算
>
>+ 或運算兩個值中只要有一個為True,就會返回True
>+ 或運算是找True，Python中的或運算是短路的或，如果第一個值是True,則不看第二個

```python
result = True or True      # True
result = True or False     # True
result = False or True     # True
result = False or False    # False

False or print('你猜我出來出來嗎?')   # print會執行
True or print('你猜我出來出來嗎?')    # print不會執行
```



### *注意事項 - 非布爾值的`and`/`or`運算

>+ 當我們對非布爾值進行與或運算時，`Python會將其當作布爾值運算，最終返回原值`。
>
>+ `and`運算規則
>
>  與運算是找false的，如果第一個是false，則不看第二個。
>
>  如果第一個值是false則直接返回第一個，否則返回第二個。
>  
>+ `or`運算規則
>
>   或運算是找true的，如果第一個是true，則不看第二個。
>
>   如果第一個值是true則直接返回第一個，否則返回第二個值。   

```python
result = 1 and 2    # 2
result = 1 and 0    # 0
result = 0 and 1    # 0
result = 0 and None    # 0 

result = 1 or 2  # 1
result = 1 or 0  # 1
result = 0 or 1  # 1

result = 0 or None  # None
```

## 5-5. 三目運算符(條件運算符)

### 語法: `語句1 if 條件達式 else 語句2`

>執行流程:
>
>​	條件運算符在執行時，會先對條件表達式進行判斷。
>
>如果判定結果為true，則執行語句1，並返回執行結果
>
>如果判定結果為false，則執行語句2，並返回執行結果

```python
# print("你好") if True else print("Hello")
a = 10
b = 20
# print('a的值比較大') if a > b else print('a的值比較小')
max = a if a > b else b
print(max) # 20
```

## 5-6. 運算符優先級

+ 優先順序為上至下

| 運算符號                                     | 表示          |
| :------------------------------------------- | :------------ |
| ()                                           | 括號          |
| **                                           | 指數          |
| +x, -x, ~x                                   | 正、負、倒數  |
| *, /, //, %                                  | 乘、除、餘數  |
| +, -                                         | 加、減        |
| <<, >>                                       | 位元 SHIFT    |
| &                                            | 位元 AND      |
| ^                                            | 位元 XOR      |
| \|                                           | 位元 OR       |
| ==, !=, >, >=, <, <=, is, is not, in, not in | 邏輯 比較符號 |
| not                                          | 邏輯 NOT      |
| and                                          | 邏輯 AND      |
| or                                           | 邏輯 OR       |

> ​	和數學中一樣，在Python運算也有優先級，比如先乘除後加減。運算符的優先級可以根據優先級的表格來查詢，在表格中位置越靠上的運算符優先級越高，優先級越高的越優先計算，如果優先級一樣則自左向右計算，關於優先級的表格，你知道有這麼一個東西就夠了，千萬不要去記，在開發中如果越到優先級不清楚的，則可以通過小括號來改變運算順序。



<span alt="solid">範例: 05_運算符</span>



---

# 6. 條件判斷

## 6-1. `input`函數

+ 用來獲取用戶輸入

>1. input函數調用後程序會立即暫停，等待用戶輸入。用戶輸入內容後，點擊回車程序才會繼續往下執行，用戶輸入完成以後，其所`輸入的內容會以返回值的型式返回`，input()的`返回值是一個字符串`
>
>2. input()函數中可以設置一個字符串作為參數，這個字符串將會作為提示文字顯示。

```python
userName = input("請輸入用戶名:")

if userName == 'admin':
    print('歡迎管理員登陸')

```

## 6-2. 條件判斷`if`

+ 條件判斷語句(if語句)

>if `條件表達式`:
>	`代碼塊`

>執行的流程: 
>
>if語句在執行時，會先對條件表達式進行求值判斷,
>
>如果為True，則執行if後的語句
>
>如果為False。則不執行
>
>1. 默認情況下,if語句只會控制緊隨其後的那條語句。如果希望if可以控制多條語句，則可以在if後面跟著一個代碼塊。
>
>2. `代碼塊`:
>代碼塊中保存著一組代碼，同一個代碼塊中的代碼，要嘛都執行要嘛都不執行
>代碼塊就是一種為代碼分組的機制
>如果要編寫代碼塊，語句就不能緊隨其後，而是要寫在下一行
>代碼塊以縮進開始，直到代碼恢復到之前的縮進級別時結束

```python
if True: print('你猜我出來嗎?')

num = 10
if num > 10: print('num比10大')

if False:
    print(123)
    print(456)
    print(789)

num = 28

# 可以使用邏輯運算符來連接多個條件
# 如果希望所有條件同時滿足，則需使用and
# 如果只要有一個條件滿足即可，則需使用or

if num> 10 and num<20:
    print("num比10大,num比20小")
```

## 6-3. `if-else`

>if `條件表達式`:
>           `代碼塊`
>     
>     else:
>            `代碼塊`

>執行流程: 
>
>if-else在執行時，先對if後的條件表達式進行求值判斷
>
>如果為True，則執行if後的代碼塊
>
>如果為False，則執行else後的代碼塊

```python
# 讓用戶在控制台中輸入一個年齡
age = input('請輸入你的年齡:')

# 如果用戶大於18歲，則顯示你已經成年
if int(age) >= 18:
    print('你已經成年!')
else:
    print('你還未成年!')
```

## 6-4. `if-elif-else`

>if `條件表達式`:
>
>​	`代碼塊`
>
>elif `條件表達式`:
>
>​	`代碼塊`
>
>else:
>
>​	`代碼塊`

> 執行流程:
>
>if-elif-else在執行時，會自上向下依次對條件表達式進行求值判斷。
>
>如果表達式結果為True，則執行當前代碼塊，然後語句結束。
>
>如果表達式結果為False，則繼續向下判斷，直到找到True為。
>
>如果所有表達式都為False，則執行else後的代碼塊

## 6-5. `match-case`

>match `變量名`:
>
>​	case `變量值1`:
>
>​		`代碼塊`
>
>​	case `變量值2`:
>
>​		`代碼塊`
>
>​	.
>
>​	.
>
>​	.
>
>​	case `_`:
>
>​		`代碼塊`

>執行流程:
>
> 判斷變量是否與`變量值1`相同，如果相同則執行`變量值1`下的代碼塊。
>
>如果不相同判斷變量是否與`變量值2`相同，如果相同則執行`變量值2下`的代碼塊。
>
>如果不相同判斷變量是否與`變量值3`相同，如果相同則執行`變量值3`下的代碼塊。
>
>如果變量沒有找到相同的case，則執行`case _`下方的代碼塊。

```python
name = 'CJ'


match name[0]:
    case 'A':
        print('name[0] = A')
    case 'B':
        print('name[0] = B')
    case 'C':
        print('name[0] = C')
    case _:
        print(f'default case name[0] = {name[0]}')


```



<span alt="solid">範例: 06_條件判斷</span>



---

# 7. 循環語句

## 7-1. `while`語句

+ 循環語句可以讓指定代碼塊重複執行。
+ 循環語句分為兩種  `while`循環 及`for`循環

> while `條件表達式`:
>
>​	`代碼塊`
>
>else:
>
>​	`代碼塊`

>執行流程: 
>
>while語句在執行時，會先對while後的條件表達式進行求值判斷。
>
>如果條件表達式為True，則執行循環體(代碼塊)。
>
>循環體執行完畢，繼續對條件表達式進行求值判斷，然後依此類推。
>
>直到判斷結果為False，則循環終止，如果循環有對應的else，則執行else後的代碼塊。

```python
# 循環的三個要件
# 初始化表達式，通過初始化表達式初始一個變量
i = 0
# 條件表達式，條件表達式用來設置循環執行的條件
while i < 10:
    print(i)
    # 更新表達式，用來修改初始化變量
    i += 1
```

## 7-2. `break`可以用來立即退出循環語句(包括else)

## 7-3. `continue`可以用來跳過當次循環

## 7-4. `pass`用來在判斷語句或循環語句中占位的

```python
# 創建一個五次的循環
# break
i = 0
while i < 5:
    if i == 3:
        break
    print("i=", i)
    i += 1
else:
    print("循環結束")

# continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print("i=", i)

else:
    print("循環結束")

# pass
if i < 5:
    pass

```



<span alt="solid">範例: 07_循環語句</span>



---

# 8. 序列 - 列表

>1. 列表是Python中的一個對象。
>2. 對象(object)就是內存中專門用來儲存數據的一個區域。
>3. 列表中可以保存多個有序的數據。



+    序列(sequence)

  序列是Python中最基本的數據結構，數據結構是計算機中數據存儲的方式

  序列用於保存一組有序的數據，所有的數據在序列當中都有唯一的位置(索引)
  並且序列中的數據會依照添加的順序來分配索引

+ 序列的分類
>1. 可變序列 (序列中的元素可以改變):
>
>   \- list(列表)
>
>2. 不可變序列  (序列中的元素不可以改變):
>     \- str (字符串)
>     \- tuple(元組)



## 8-1. 列表的創建 `list_name= []`

### - 當向列表中添加多個元素時，多個元素之間使用`，`隔開

### - 列表中可以存儲任意數據類型

### - 通過索引來獲取列表中的元素

### - `len()`函數可以獲取列表的長度

​	

```python
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
# len()函數，通過該元素可獲取列表的長度
# 獲取到的長度，是列表的最大索引+1
print(len(my_list))

```



## 8-2. 列表的切片

### - 列表的索引可以是負數

>如果索引是負數，則會從後向前獲取元素，-1表示倒數第一個，-2表示倒數第二個，依此類推。

###  - 通過切片來獲取指定的元素 `列表[起始:結束(不包含)]`

>語法: `列表[起始:結束(不包含)]`
>
>+ 通過切片獲取元素時，會包含起始位置元素，但不包含結束位置元素。
>+  做切片操作時，總會返回一個新的列表，`不會影響原來的列表`。
>+ 如果省略結束位置，則會一直擷取到最後。
>+ 如果省略開始位置，則會從第一個位置開始擷取。
>+  如果開始位置和結束位置都省略，相當於創建了一個列表的副本。

### - 通過切片來獲取指定的元素 `列表[起始:結束(不包含):步長]`

>語法: `列表[起始:結束(不包含):步長]`
>
>+ 步長表示，每次獲取元素的間隔，默認值為1。
>+ 步長不能是0，但可以是負數。



```python
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


```



### - *列表的傳遞是透過指針

```python
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
```



## 8-2.列表通用操作

### - `+`運算可以將兩個列表拼接為一個新的列表

```python
A = [10, 20, 30]
B = [40, 50, 60]
C= A+B
print(C)
```

### - `*`運算可以將列表重複一個指定的次數

```python
A = [10, 20, 30]
B = A*6
print(B)
```

### - `元素 [not] in 列表`  檢查指定元素是否(不)存在列表內

```python
A = [10, 20 , 30]
B = 10
C = 1
result1 =  B in A
print(result1)
result2 =  C not in A
print(result2)
```

 ### - `len()`獲取列表中的元素個素

```python
A = [10, 20 , 30]
result1 = len(A)
print(result1)
```

### - `max()/min()` 獲取列表中的最大最小值

```python
arr = [10, 1, 2, 5, 100, 77, 100]
print('max = ', max(arr), ',min=', min(arr))
```

### - `index(_value,  _start. _end)`返回列表中指定元素的索引，如果有多個相同元素，則會返回第一個索引,如果指定元素不存在會拋出異常 `ValueError: 200 is not in list`

```python
arr = [10, 1, 2, 5, 100, 77, 100]
print(arr.index(10, 3))
print(arr.index(10, 3, 5))
```

### - `count(_value)`返回列表中指定元素的個數，元素不存在，則返回0

```python
arr = [10, 1, 2, 5, 100, 77, 100]
print(arr.count(100))
```



## 8-3. 列表的修改

### - 直接通過索引來修改

```python
# 創建一個列表
stus = ['孫悟空', '豬八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']

# 修改列表中的元素
# 直接通過索引來修改元素
print('修改前:', stus)
stus[0] = 'sunwukong'
print('修改後:', stus)

```

### - 通過`del`關鍵字來刪除元素

```python
A = [1, 2 ,3]
del A[0]
print(A)
```

### - 通過切片修改列表

>1. 在給切片賦值時，只能使用序列 `TypeError: can only assign an iterable`。
>
>2. 當設置步長時，序列中的元素個數必須和切片的元素個數一致。

```python
A = [1, 4, 5]
print(A[0:1])
A[0:1] = [0]
print(A)
A[1:3] = [1, 2]
print(A)

'''
output
[1]
[0, 4, 5]
[0, 1, 2]
'''
```

### - 通過切片刪除元素`del A[::]` /`A[::] = []`

>1. `del`關鍵字配合切片來刪除
>2. `A[::] = []`通過切片刪除元素， 步長只能為1，否則報錯`ValueError: attempt to assign sequence of size 0 to extended slice of size 2`

```python
A = [1, 4, 5, 6, 7 ,8]
# 移除偶數索引
# del A[2::2]
# 通過切片刪除元素
# 1. 步長只能為1，否則報錯ValueError: attempt to assign sequence of size 0 to extended slice of size 2
A[2::1] = []
print(A)

'''
output
[1, 4, 6, 8]
# [1, 4]
'''
```

### - 不可變序列，無法通過索引來修改，可以通過`list()`函數將其他序列轉換為list

```python
s = 'hello'
# s[0] = 1
# print(s)
s1 = list(s)
s1[0] = '1'
print(''.join(s1))

'''
output
# TypeError: 'str' object does not support item assignment
1ello
'''
```

> `'合併符號'join(Iterable[LiteralString])`: 可以將字符串列表合併為一個字串。



## 8-4. 列表的方法

### - `append()` 向列表最後添加一個元素

```python
stus = ['孫悟空', '豬八戒', '沙和尚']
print('原列表:', stus)
stus.append('唐僧')   # 等同stus[len(stus):len(stus)] = ['唐僧']
print('新列表:', stus)
```

### - `insert(_index. _object)`向列表指定位置插入一個元素

```python
stus = ['孫悟空', '豬八戒', '沙和尚']
stus.insert(1, '唐僧')
print('新列表:', stus)
```

### - `extend(__iterable)`使用新序列來擴展當前序列，它會將該序列中的元素添加到當前列表

```python
stus = ['孫悟空', '豬八戒', '沙和尚']
stu2s = ['Jeff', 'Amy']
stus.extend(stu2s)      # stus += stu2s
print('新列表:', stus)
```

### - `clear()`清空序列

```python
stus = ['孫悟空', '豬八戒', '沙和尚']
stus.clear()
print('新列表:', stus)
```

### - `pop(__index)`根據索引刪除並返回被刪除元素

```python
stus = ['孫悟空', '豬八戒', '沙和尚']
del_element = stus.pop(2)     # 刪除索引為2的元素
print('新列表:', stus, '被刪除元素:', del_element)
```

### - `remove(__value)`刪除指定元素，如果相同值有多個，它只會刪除第一個

```python
stus = ['孫悟空', '豬八戒', '沙和尚', '孫悟空']
stus.remove('孫悟空')
print('新列表:', stus)
```

### - `reverse()` 反轉列表

```python
stus = ['孫悟空', '豬八戒', '沙和尚']
stus.reverse()
print('新列表:', stus)
```

### -`sort(key, reverse)`用來對列表中元素進行排序，默認是升序排序, 如果需要降序排列，則需要傳遞一個`reverse=True`作為參數

```python
A = [10, 7, 5, 1, 6]
# 默認是升序
A.sort()
print(A)
# 關鍵字參數reverse=True來達到降序
A.sort(reverse=True)
print(A)

A = [10, 7, 5, 1, 6]
# 練習: 使用key關鍵字參數來對索引做排序
A_index = list(range(len(A)))
print(A_index)
A_index.sort(key=lambda x: A[x])
print(A_index)
```



## 8-5. 列表的遍歷

### - `for` 迴圈遍歷列表，指的就是將列表所有元素取出。

>通過for循環來遍歷列表
>
>語法:
>
>​	 for `變量` in `列表`:
>
>​		  `代碼塊`
>
>說明:
>
>for循環的代碼塊會執行多次，序列中有幾個元素就會執行幾次
>
>每執行一次就會將序列中的元素賦值給變量
>
>所以我們可以通過變量，來獲取列表中的元素

### - `for`循環除了創建方式以外，其餘都和`while`一樣，包括`else`、`break`、`continue`都可以在`for`循環使用

```python
# 創建列表
stus = ['孫悟空', '豬八戒', '沙和尚', '唐僧']

for stu in stus:
    print(stu)
```



## 8-6. `range(起始位置:結束位置(不包含):步長)`函數

### -可以用來生成一個自然數的序列

```python
r1 = range(5)   # 生成一個[0, 1, 2, 3 ,4]
print(list(r1))

# 該函數需要三個參數
#   1.起始位置: 可以省略，默認是0
#   2.結束位置(不包含)
#   3.步長:  可以省略，默認是1
r2 = range(1, 10, 2)
print(list(r2))
r3 = range(10, 0, -3)
print(list(r3))

'''
output
[0, 1, 2, 3, 4]
[1, 3, 5, 7, 9]
[10, 7, 4, 1]
'''
```



<span alt="solid">範例: 08_列表</span>



---

# 9. 序列 - 元組tuple

## 9-1. 元組的創建 `tuple_name= ()`

### - 元組是一個`不可變的序列`

### - 所以在操作元組時，就把元組當成一個`不可變的列表`

### - 一般當我們希望數據不改變時，就使用元組，其餘情況都使用列表

```python
# 創建元組
# 使用()來創建元組
t = ()  # 創建一個空元組
print(type(t))

my_tuple = (1, 2, 3, 4, 5)  # 創建一個五個元素的元組
print(my_tuple)
print(my_tuple[3])
# 元組是不可變對象，不能嘗試對元組中的元素重新賦值
# my_tuple[3] = 1  TypeError: 'tuple' object does not support item assignment

```

### - 當元組不是空元組時，括號可以省略。如果元組不是空元組，它裡邊至少要一個逗號,

```python
my_tuple = 1, 2, 3, 4, 5
my_tuple = 10,
print(my_tuple)
```

##  9-2. [重要]序列解包操作

### - 1對1分離 `a, b, c, d = my_tuple`

>在對元組進行解包時，變量的數量需要和元組中的元素數量一致。

```python
my_tuple = (10, 20, 30, 40)
a, b, c, d = my_tuple
print('a=', a)
print('b=', b)
print('c=', c)
print('d=', d)

'''
output
a= 10
b= 20
c= 30
d= 40
'''
```

### - 1對1分離 & 1對多分離  `a, b, *c = my_tuple`

>可以在變量前面加一個*，這樣變量將會獲取元組中剩餘的所有元素。

```python
my_tuple = 1, 2, 3, 4, 5
a, b, *c = my_tuple
print('c = ', c)
a, *b, c = my_tuple
print('b = ', b)

'''
output
c =  [3, 4, 5]
b =  [2, 3, 4]
'''
```

### - [應用]交換a和b的值，這時我們就可以利用元組的解包 `a, b = b, a`

```python
a = 20
b = 40
b, a= a, b
print(f'a= {a}')
print(f'b= {b}')

```



<span alt="solid">範例: 09_元組</span>



---

# 10. 可變對象

## 10-1. 對象中包含`id`/`type`/`value`

>1. 每個對象都保存了三個數據:
>     \- id(標誌)
>     \- type(類型)
>     \- value(值)
> 1. 列表就是一個可變對象
>     a = [1, 2, 3]
>

## 10-2. 改對象值

>1. 變量所指向的對象定址不會改變，只改變對象內的內容。
>2. 當我們去修改對象時，如果有其他變量也指向該對象，則修改也會在其他變量中體現。

```python
a = [1, 2, 3]
print('a指向的對象=', id(a))
a[0] = 10
print('a指向的對象=', id(a))
```

## 10-3. 更改變量所指向的對象

>1. 變量所指向的對象定址會改變。
>2. 一般只有在為變量賦值時才是修改變量，其餘都是在修改對象。

```python
a = [1, 2, 3]
print('a指向的對象=', id(a))
a = [10, 2, 3]
print('a指向的對象=', id(a))
```

## 10-4. `is [not]`比較是否是同一個對象(注意與`==`/`!=`差異)

>1. `is`比較的是對象`id`是否相同。
>2. `==`比較的是對象`value`是否相同。

```python
# ==, !=, is, is not
# == , != 比較的是對象的值是否相等
# is , is not  比較的是對象的id是否相等
a = [1, 2, 3]
b = [1, 2, 3]
print('a==b?', a == b)   # a和b值相等，會返回True
print('a is b?', a is b) # a和b不是同一個對象，會返回False
b = a
print('a==b?', a == b)
print('a is b?', a is b)
```



<span alt="solid">範例: 10_可變對象</span>

 

---

# 11. 序列 - 字典`dict`

## 11-1. 字典(dict)簡介

### - 字典屬於一種新的數據結構，稱之為映射(mapping)

### \- 字典的作用和列表類似，都是用來儲存對象的容器

### \- *列表存儲數據的性能很好，但查詢數據的性能很差

### -在字典中每一個元素都有唯一的名字，通過這個唯一的名子可以快速地查找到指定的元素

### - 在查詢元素時，字典的效率是非常快的

### - 字典中也是可以保存多個對象，每個對象都會有一個唯一的名子，我們也稱為鍵值對結構(key-value)

> 字典中也是可以保存多個對象，每個對象都會有一個唯一的名子。這個唯一的名子,我們稱之為key(鍵)，通過key可以快速查找value。這個對象，我們稱其為value(值)。所以字典，我們也稱為鍵值對結構(key-value)。每個字典中都可以有多個鍵值對，而每一個鍵值對，我們稱值為item。



## 11-2.  創建字典

### \- 使用`{}`/`dict()`來創建一個空字典

```python
# 創建一個空字典
# 使用{}來創建字典
my_dict = {}
# my_dict = dict()
print(type(my_dict))
```

### \- `{key: value, key: value, key: value..}`創建一個有數據的字典

>語法:
>
>​	{key: value, key: value, key: value..}
>
>1. 字典的值可以是任意對象
>
>2. 字典的key可以是任意的不可變對象(`int`、`str`、`bool`、`tuple`...)，但一般我們都會使用`str`
>3. 字典的key是不能重複的，如果出現重複的，後面會替換到前邊的

```python
d = {'name': '孫悟空', 'age': 18, 'gender': '男'}
print(d)
```

### \- 根據鍵來獲取值`dict_var['key']`

```python
# 可以根據鍵來獲取值
print(d['name'], d['age'], d['gender'])
# 如果使用字典中不存在的鍵值，會抱錯
# print(d['hello'])  KeyError: 'hello'
```



## 11-3. 字典使用

### \- 使用dict()函數來創建字典 `d = dict(name='孫悟空', age=18, gender='男')`
```python
d = dict(name='孫悟空', age=18, gender='男')
print(d, type(d))
```

### - 可以將一個`雙值子序列`的序列轉換為字典

```python
d = dict([('name', '孫悟空'), ('age', 18), ('gender', '男')])
print(d, type(d))
```

### \- `len()`函數 獲取字典內鍵值對的個數

```python
d = dict([('name', '孫悟空'), ('age', 18), ('gender', '男')])
print(len(d))
```

### \- `[not] in` 檢查字典內是否有包含指定的`key`

```python
d = dict([('name', '孫悟空'), ('age', 18), ('gender', '男')])
print('name' in d)
print('aaa' not in d)
```

### \- `get(key[, default])` 該方法用來根據鍵獲取字典的值, 如果獲取的鍵在不在字典中，則返回none。也可以指定一個默認值，來作為第二個參數，這樣獲取不到值時，會返回默認值。

```python
d = dict([('name', '孫悟空'), ('age', 18), ('gender', '男')])
print(d.get('aaa', '默認值'))
```

### \- `d[key] = value` 修改/新增字典, 如果key存在則覆蓋，不存在則添加。

```python
d = dict([('name', '孫悟空'), ('age', 18), ('gender', '男')])
d['name'] = 'Jeff'
print(d)
d['address'] = '花果山'
print(d)
```

### \-  `setdefault(key[, default])` 可以用來向字典中添加鍵字對，如果鍵值存在則不會覆蓋，鍵值不存在就會添加key-value。

```python
d = dict([('name', '孫悟空'), ('age', 18), ('gender', '男')])
d.setdefault('電話', '1111')
print(d)
```

### \- `update([dict])`將其他字典中的key-value，添加到當前字典中，如果有重複的key，後面的會替換當前的。

```python
d = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 6, 'f': 6, 'a': '7'}
d.update(d2)
print(d)
```

### \- `del dict_name[key]`用來刪除字典中的key-value，如果刪除不存在的key，它會拋出異常。

```python
d = {'a': 1, 'b': 2, 'c': 3}
del d['a']
del d['b']
print(d)
```

### \-  `popitem()`隨機刪除字典中的鍵值對，一般會刪除最後一個鍵值對。 刪除之後，它會將刪除的key-value做為返回值返回。返回的是一個元組，元組中有兩個元素，第一個是刪除的key，第二個是刪除的value。當使用`popitem`刪除一個空字典時，會拋出異常`KeyError: 'popitem(): dictionary is empty'`。

```python
d = {'a': 1, 'b': 2, 'c': 3}
result = d.popitem()
print(result)
```

### \-  `pop(key[, default])` 根據key刪除字典中的key-value，會將被刪除的value返回。如果刪除不存在的key，它會拋出異常。如果指定了默認值，再刪除不存在的key，不會報錯，而是直接返回默認值。

```python
d = {'a': 1, 'b': 2, 'c': 3}
result = d.pop('e')
result = d.pop('z', '默認值')
```

### \- `clear()` 用來清空字典

```python
d = {'a': 1, 'b': 2, 'c': 3}
d.clear()
print('result=', d)
```

### \- *`copy()` 該法方用來對字典進行淺複製，複製以後的對象和原對象是獨立，修改一個不會影響另一個， 注意，淺複製只會簡單複製對象內的值，如果值也是一個可變對象，這個可變對象不會被複製。

```python
d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d
d2 = d.copy()
print('d=', '{:#x}'.format(id(d)))
print('d2=', '{:#x}'.format(id(d2)))

d = {'a': {'name': 'Jeff', 'age': 18, 'gender': '男'}, 'b': 2, 'c': 3}
d2 = d.copy()
d2['a']['name'] = '豬八戒'
print(d)
print(d2)

print("d['a']", '{:#x}'.format(id(d["a"])))
print("d2['a']",'{:#x}'.format(id(d2['a'])))
'''
d= 0x2a2b01e8d00
d2= 0x2a2b02ab4c0
{'a': {'name': '豬八戒', 'age': 18, 'gender': '男'}, 'b': 2, 'c': 3}
{'a': {'name': '豬八戒', 'age': 18, 'gender': '男'}, 'b': 2, 'c': 3}
d['a'] 0x2a2b02ab100
d2['a'] 0x2a2b02ab100
'''
```



## 11-4. 遍歷字典

### - `keys()` 該方法會返回一個序列，序列中保存所有字典的key，通過遍歷`keys()`來獲取所有鍵。

```python
d = {'name': '孫悟空', 'age': 18, 'gender': '男'}
# 通過遍歷keys()來獲取所有鍵
for key in d.keys():
    print(key, d[key])
```

### \- `values()` 該方法會返回字典的所有value

```python
d = {'name': '孫悟空', 'age': 18, 'gender': '男'}
for value in d.values():
    print(value)
```

### \- `items()` 該方法會返回字典中的所有項，它會返回一個序列，序列中包含雙值子序列  `[(k1,v1),(k2,v2),....]`

```python
d = {'name': '孫悟空', 'age': 18, 'gender': '男'}
for k, v in d.items():
    print(k, v)
```



<span alt="solid">範例: 11_字典</span>



---

# 12. 序列 - 集合`set`

>集合和列表非常相似
>
>不同點:
>
>1. 集合只能儲存不可變對象。
>2. 集合中儲存的對象是無序的(不是按照元素的插入順序保存)。
>3. 集合中不能出現重複的元素。



## 12-1. 創建集合

### \- 使用`{}`來創建集合，只能儲存不可變對象。

```python
s = {1, 10, 3, 4, 5}
# s = {[1, 2, 3], [4, 5, 6]} TypeError: unhashable type: 'list'
print(s, type(s))
```

### \- 用`set()`函數來創建集合

```python
s = set()   # 創建空集合
```

### \- 可以通過`set()`來將序列和字典轉換為集合

```python
s1 = set([1, 3, 5, 6, 7, 7, 8])
print(s1)
s2 = set('aadakjf;f')
print(s2)
s3 = set({'a': 1, 'b': 2, 'c': 3})
print(s3)
'''
output
{1, 3, 5, 6, 7, 8}
{';', 'd', 'a', 'k', 'f', 'j'}
{'b', 'a', 'c'}
'''
```

## 12-2. 集合的使用

###  \-  使用`in`和`not in`來檢查集合中元素

```python
s = {'a', 'b', 'c'}
print('c' in s)
```

### \- `len()`來獲取集合中的元素數量

### \- `add()`向集合中添加元素

```python
s = {'a', 'b', 'c'}
s.add('f')
print(s)
```

### \- `update()` 將一個集合中的元素，添加到當前集合中

```python
# update() 將一個集合中的元素，添加到當前集合中
# update()可以傳遞序列和字典作為參數，字典只會使用鍵
s1 = set('abc')
print(s1)
s2 = set(('aaa', 20, 30, 40, 50))
s1.update(s2)
print(s1)

'''
output
{'c', 'a', 'b'}
{'c', 40, 50, 'a', 20, 'aaa', 30, 'b'}
'''
```

### \- `pop()` 隨機刪除集合中的一個元素並返回刪除元素

```python
s = set('abcde')
ds = s.pop()
print(f's = {s}, del = {ds}')
```

### \- remove() 刪除集合中的指定元素，元素不存在會報錯 `KeyError: '100'`

```python
s1 = {1, 2 ,3}
tmp = s1.remove(1)
print(s1, tmp)
'''
output
{2, 3} None
'''
```

### \- `clear()` 清空集合

### \- `copy()` 對集合進行淺複製

## 12-3. 集合運算

### - `&`交集

```python
s = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
result = s & s2
print(result)
'''
output
{3, 4, 5}
'''
```

### - `|`並集

```python
s = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
result = s | s2
print(result)
'''
output
{1, 2, 3, 4, 5, 6, 7}
''''''
```

### \- `-`差集

```python
s = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
result = s2 - s
print(result)
'''
output
{6, 7}
'''
```

### \- `^`亦或集(獲取不相交部分, 獲取只在一個集合出現的元素)

```python
s = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
result = s2 ^ s
print(result)
'''
output
{1, 2, 6, 7}
'''
```

### \- `<=` 檢查一個集合是否是另一個集合的子集

```python
s = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}
result = s2 <= s
print(result)
'''
output
True
'''
```

### \- `<` 檢查一個集合是否是另一個集合的真子集

```python
result = {1, 2, 3} < {1, 2, 3}
print(result)
'''
output
False
'''
```

### \- `>=` 檢查一個集合是否是另一個集合的超集

### \- `>` 檢查一個集合是否是另一個集合的真超集



<span alt="solid">範例: 12_集合</span>



---



# 教學資源

https://www.youtube.com/watch?v=K2EZ-beTdGM&list=PLmOn9nNkQxJFGvtKd7PI7AhsYmY-6FrJs&index=100