

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



 

# 教學資源

https://www.youtube.com/watch?v=K2EZ-beTdGM&list=PLmOn9nNkQxJFGvtKd7PI7AhsYmY-6FrJs&index=100