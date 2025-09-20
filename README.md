

[TOC]

---

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

# 2. 數據類型(變量值讀類型)

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
>   調用方法來將變量轉換類型，函數不會對原來的變量產生影響，它是`將對象轉換為指定類型並作為返回值返回`。因此如果希望修改原先變量，則需要重新賦值。



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
>   - list(列表)
>
>2. 不可變序列  (序列中的元素不可以改變):
>     - str (字符串)
>     - tuple(元組)



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

### - `index(_value,  _start, _end)`返回列表中指定元素的索引，如果有多個相同元素，則會返回第一個索引,如果指定元素不存在會拋出異常 `ValueError: 200 is not in list`

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

### - `sort(key, reverse)`用來對列表中元素進行排序，默認是升序排序, 如果需要降序排列，則需要傳遞一個`reverse=True`作為參數

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
>     - id(標誌)
>     - type(類型)
>     - value(值)
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

### - 字典的作用和列表類似，都是用來儲存對象的容器

### - *列表存儲數據的性能很好，但查詢數據的性能很差

### - 在字典中每一個元素都有唯一的名字，通過這個唯一的名子可以快速地查找到指定的元素

### - 在查詢元素時，字典的效率是非常快的

### - 字典中也是可以保存多個對象，每個對象都會有一個唯一的名子，我們也稱為鍵值對結構(key-value)

> 字典中也是可以保存多個對象，每個對象都會有一個唯一的名子。這個唯一的名子,我們稱之為key(鍵)，通過key可以快速查找value。這個對象，我們稱其為value(值)。所以字典，我們也稱為鍵值對結構(key-value)。每個字典中都可以有多個鍵值對，而每一個鍵值對，我們稱值為item。



## 11-2.  創建字典

### - 使用`{}`/`dict()`來創建一個空字典

```python
# 創建一個空字典
# 使用{}來創建字典
my_dict = {}
# my_dict = dict()
print(type(my_dict))
```

### - `{key: value, key: value, key: value..}`創建一個有數據的字典

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

### - 根據鍵來獲取值`dict_var['key']`

```python
# 可以根據鍵來獲取值
print(d['name'], d['age'], d['gender'])
# 如果使用字典中不存在的鍵值，會抱錯
# print(d['hello'])  KeyError: 'hello'
```



## 11-3. 字典使用

### - 使用dict()函數來創建字典 `d = dict(name='孫悟空', age=18, gender='男')`
```python
d = dict(name='孫悟空', age=18, gender='男')
print(d, type(d))
```

### - 可以將一個`雙值子序列`的序列轉換為字典

```python
d = dict([('name', '孫悟空'), ('age', 18), ('gender', '男')])
print(d, type(d))
```

### - `len()`函數 獲取字典內鍵值對的個數

```python
d = dict([('name', '孫悟空'), ('age', 18), ('gender', '男')])
print(len(d))
```

### - `[not] in` 檢查字典內是否有包含指定的`key`

```python
d = dict([('name', '孫悟空'), ('age', 18), ('gender', '男')])
print('name' in d)
print('aaa' not in d)
```

### - `get(key[, default])` 該方法用來根據鍵獲取字典的值, 如果獲取的鍵在不在字典中，則返回none。也可以指定一個默認值，來作為第二個參數，這樣獲取不到值時，會返回默認值。

```python
d = dict([('name', '孫悟空'), ('age', 18), ('gender', '男')])
print(d.get('aaa', '默認值'))
```

### - `d[key] = value` 修改/新增字典, 如果key存在則覆蓋，不存在則添加。

```python
d = dict([('name', '孫悟空'), ('age', 18), ('gender', '男')])
d['name'] = 'Jeff'
print(d)
d['address'] = '花果山'
print(d)
```

### - `setdefault(key[, default])` 可以用來向字典中添加鍵字對，如果鍵值存在則不會覆蓋，鍵值不存在就會添加key-value。

```python
d = dict([('name', '孫悟空'), ('age', 18), ('gender', '男')])
d.setdefault('電話', '1111')
print(d)
```

### - `update([dict])`將其他字典中的key-value，添加到當前字典中，如果有重複的key，後面的會替換當前的。

```python
d = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 6, 'f': 6, 'a': '7'}
d.update(d2)
print(d)
```

### - `del dict_name[key]`用來刪除字典中的key-value，如果刪除不存在的key，它會拋出異常。

```python
d = {'a': 1, 'b': 2, 'c': 3}
del d['a']
del d['b']
print(d)
```

### - `popitem()`隨機刪除字典中的鍵值對，一般會刪除最後一個鍵值對。 刪除之後，它會將刪除的key-value做為返回值返回。返回的是一個元組，元組中有兩個元素，第一個是刪除的key，第二個是刪除的value。當使用`popitem`刪除一個空字典時，會拋出異常`KeyError: 'popitem(): dictionary is empty'`。

```python
d = {'a': 1, 'b': 2, 'c': 3}
result = d.popitem()
print(result)
```

### - `pop(key[, default])` 根據key刪除字典中的key-value，會將被刪除的value返回。如果刪除不存在的key，它會拋出異常。如果指定了默認值，再刪除不存在的key，不會報錯，而是直接返回默認值。

```python
d = {'a': 1, 'b': 2, 'c': 3}
result = d.pop('e')
result = d.pop('z', '默認值')
```

### - `clear()` 用來清空字典

```python
d = {'a': 1, 'b': 2, 'c': 3}
d.clear()
print('result=', d)
```

### - *`copy()` 該法方用來對字典進行淺複製，複製以後的對象和原對象是獨立，修改一個不會影響另一個， 注意，淺複製只會簡單複製對象內的值，如果值也是一個可變對象，這個可變對象不會被複製。

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

### - `values()` 該方法會返回字典的所有value

```python
d = {'name': '孫悟空', 'age': 18, 'gender': '男'}
for value in d.values():
    print(value)
```

### - `items()` 該方法會返回字典中的所有項，它會返回一個序列，序列中包含雙值子序列  `[(k1,v1),(k2,v2),....]`

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

### - 使用`{}`來創建集合，只能儲存不可變對象。

```python
s = {1, 10, 3, 4, 5}
# s = {[1, 2, 3], [4, 5, 6]} TypeError: unhashable type: 'list'
print(s, type(s))
```

### - 用`set()`函數來創建集合

```python
s = set()   # 創建空集合
```

### - 可以通過`set()`來將序列和字典轉換為集合

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

###  -  使用`in`和`not in`來檢查集合中元素

```python
s = {'a', 'b', 'c'}
print('c' in s)
```

### - `len()`來獲取集合中的元素數量

### - `add()`向集合中添加元素

```python
s = {'a', 'b', 'c'}
s.add('f')
print(s)
```

### - `update()` 將一個集合中的元素，添加到當前集合中

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

### - `pop()` 隨機刪除集合中的一個元素並返回刪除元素

```python
s = set('abcde')
ds = s.pop()
print(f's = {s}, del = {ds}')
```

### - `remove()` 刪除集合中的指定元素，元素不存在會報錯 `KeyError: '100'`

```python
s1 = {1, 2 ,3}
tmp = s1.remove(1)
print(s1, tmp)
'''
output
{2, 3} None
'''
```

### - `clear()` 清空集合

### - `copy()` 對集合進行淺複製

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

### - `-`差集

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

### - `^`亦或集(獲取不相交部分, 獲取只在一個集合出現的元素)

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

### - `<=` 檢查一個集合是否是另一個集合的子集

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

### - `<` 檢查一個集合是否是另一個集合的真子集

```python
result = {1, 2, 3} < {1, 2, 3}
print(result)
'''
output
False
'''
```

### - `>=` 檢查一個集合是否是另一個集合的超集

### - `>` 檢查一個集合是否是另一個集合的真超集



<span alt="solid">範例: 12_集合</span>



---

# 13. 函數

## 13-1. 函數簡介

### - 定義函數`def`

>  函數是將一段可重用的邏輯封裝成獨立單元。透過呼叫函數名稱並傳入參數，可以避免重複程式碼、提升可讀性與可維護性。

```python
def func_name(param1, param2=default, *args, **kwargs):
    """
    可選的文件字串，說明函數用途、參數與返回值
    """
    # 函數主體
    return result
```

>[!NOTE]
>
>1. 函數名必須符合標識符規範(可以包含字母、數字、下划線，但不能以數字開頭)。
>
>2. 函數中保存的代碼不會立即執行，需要調用函數才會執行。
>3. 調用函數 函數名()

#### - 形參與實參: `有幾個形參就要傳遞幾個實參`

>1. 在定義函數時，可以在函數名後的()中定義數量不等的形參，多個形參之間使用，隔開。
>2. 形參(形式參數)，定義形參就相當於在函數內部聲明了變量，但不賦值
>3. 實參(實際參數)，如果在函數創建時定義了形參，那麼在函數調用時也必須傳遞實參，實參將會賦值給對應的形參，簡單來說，`有幾個形參就要傳遞幾個實參`。

```python
# 定義一個求任意兩數和的函數
def sum(x, y):
    print(x+y)

sum(1, 2)

```



## 13-2. 函數的參數

### 13-2-1. 位置參數`args`

#### - 對應位置的實參複製給對應位置的形參

>  位置參數就是將對應位置的實參複製給對應位置的形參。一個實參賦值給第一個位置的形參、 第二個實參賦值給第二個位置的形參，依此類推。

```python
def fn(a, b, c=):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    
fn(1, 2, 3)
```

#### - 定義形參時，可以為形參指定默認值

>[!NOTE]
>
>指定了默認值以後，如果用戶傳遞了參數則默認值不起作用。如果用戶沒有傳遞，則默認值就會生效。有默認值形參一定樣擺在後面，不可以def function(a, b=20, c)這樣定義。

```python
def fn(a, b, c=20):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    
fn(1, 2)
```



### 13-2-2. 關鍵字參數`kwargs`

#### - 直接根據參數名去傳遞

>  關鍵字參數，可以不按照形參定義的順序去傳遞，而是`直接根據參數名去傳遞`

```python
def fn(a, b, c=20):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    
fn(a=1, b=2, c=3)
```

#### - 和位置參數可以混合使用

#### - 混合使用時，`位置參數必須寫在前面`

>  混合使用位置參數和關鍵字參數時，必須將`位置參數寫在前面`。



```python
def fn(a, b, c=20):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    
fn(10, c=10, b=100)  
```



### 13-2-3. 實參傳遞的類型

#### - `實參可以傳遞任意數據類型`，包括函數

```python
def fn(a, b, c=20):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)

def fn2(a):
    print('a=', a)
    
fn2(fn)

# a= <function fn at 0x000001FF475CE020>
```



#### - *實參傳遞可變對象，重新賦值，不會影響其他變量



```python
def fn(a):
    # 在函數中對形參進行重新賦值，不會影響其他變量
    a = [4, 5, 6]
    print('a= {}, id= {:#018x}'.format(a, id(a)))

a = [1, 2, 3]
print('a= {}, id= {:#018x}'.format(a, id(a)))
fn(a)
print('a= {}, id= {:#018x}'.format(a, id(a)))

'''
a= [1, 2, 3], id= 0x0000024b686d51c0
a= [4, 5, 6], id= 0x0000024b687dce80
a= [1, 2, 3], id= 0x0000024b686d51c0
'''
```



#### - *實參傳遞可變對象，修改對象會影響到所有指向該對象的變量

```python
# a是可變
def fn(a):
    # a是一個列表，嘗試修改列表中的元素
    # 如果形參執行的是一個對象，當我們通過形參去修改對象時
    # 會影響到所有指向該對象的變量
    a[0] = 20

a = [1, 2, 3]
print('a= {}, id= {:#018x}'.format(a, id(a)))
fn(a)
print('a= {}, id= {:#018x}'.format(a, id(a)))

'''
a= [1, 2, 3], id= 0x0000024b687dce80
a= [20, 2, 3], id= 0x0000024b687dce80
'''
```



## 13-3. 不定長參數

>  函數在定義時可接收不定長度的參數，以便處理數量不固定的輸入。

| 語法       | 描述                 | 回傳類型 |
| ---------- | -------------------- | -------- |
| `*args`    | 收集額外的位置參數   | tuple    |
| `**kwargs` | 收集額外的關鍵字參數 | dict     |

### 13-3-1. 不定長位置參數`*args`

>  *a會接收所有的位置實參，並統一將這些`實參保存在一個元組`中(裝包)。

#### - args為tuple類型

```python
# *a會接收所有的位置實參，並統一將這些實參保存在一個元組中(裝包)
def fn2(*a):
    temp = 0
    for i in a:
        temp += i
    print(temp)

fn2(1,2,3,4,5,6)
```

#### - 不定長位置參數不是必須寫在最後，但是注意，`帶*的參數後的所有參數，必須以關鍵字參數的形式傳遞`

```python
# 第一個參數給a，剩下的位置參數給b元組，c必須使用關鍵字參數傳遞
def fn3(a, *b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)
fn3(1, 2, 3, c=4)

# 所有位置參數都給a元組，b和c需要使用關鍵字參數傳遞
def fn4(*a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)
fn4(1, 2, b=3, c=4)

# 如果在形參開頭直接寫一個*，則要求我們所有的參數必須以關鍵字參數的形式傳遞
def fn5(*, a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)

fn5(a=1 ,b=3, c=4)

```

### 13-3-2. 不定長關鍵字參數`**kwargs`

>  \**形參可以接收其他的關鍵字參數，它會將這些`參數統一保存到一個字典`中，字典的key就是參數的名字，字典的value就是參數的值，`**參數只能有一個，並且必須寫在所有參數的最後`。

#### - kwargs為dict類型

```python
def fn(b, c, **a):
    print('b=', b)
    print('c=', c)
    print('a=', a)

fn(a=1, b=3, c=10, d=10)
'''
b= 3
c= 10
a= {'a': 1, 'd': 10}
'''
```

#### - `**參數只能有一個，並且必須寫在所有參數的最後`



### 13-3-3. 參數的解包(拆包)

+ 解包的基本概念

>1. 使用 `*` 可以將可疊代對象（如 list、tuple）拆解成位置參數；
>2. 使用 `**` 可以將字典拆解成關鍵字參數。
>
>呼叫者只需要把既有的序列或映射與 `*`、`**` 一並傳入函數，Python 會自動展開。

#### - `*`拆解成位置參數(list, tuple)

```python
li = ['A', 'B', 'C']

def fn(*a):
    print(a)

fn(li)
# (['A', 'B', 'C'],)

fn(*li)
# ('A', 'B', 'C')
```



#### - `**`拆解成關鍵字參數(dict)

```python
d = {'A': 10, 'B':20, 'C': 30}

def fn2(**kwargs):
    print(kwargs)

# 報錯必須全部用關鍵字參數
# fn2(d)

fn2(**d)
# {'A': 10, 'B': 20, 'C': 30}
```



## 13-4. 函數返回值

### - `return`關鍵字

### - return一執行函數自動結束

### - 可以return任意數據類型，返回值可以是函數，如果只寫一個return或不寫return，則相當於return None

>  返回值就是函數執行以後返回的結果，可以通過`return`來指定函數的返回值, return之後可以跟任意數據類型，返回值甚至可以是一個函數，如果只寫一個return或不寫return，則相當於return `None`。在函數中，return後的代碼都不會執行，`return一執行函數自動結束`。



```python
def sum(*nums):
    # 定義一個變量保存結果
    result = 0
    # 遍歷元組，並將元組中的元素進行累加
    for num in nums:
        result += num
    return result

print(sum(123, 456, 789))


def fn():
    return 10

# fn和fn()的區別
print(fn)       # fn是函數對象，打印fn實際是在打印函數對象    <function fn at 0x0000013C1A2E8860>
print(fn())     # fn()是在調用函數，打印fn()實際是在打印fn()函數的返回值
```



## 13-5. 文檔字符串

### - 函數的第一行寫下的字符串就是文檔字符

> 文檔字符串(doc str)
>
> 在定義函數時，可以在函數內部編寫文檔字符串，文檔字符串就是函數的說明， 當我們編寫了文檔字符串，我們就可以通過help()函數來查看函數的說明
>
> 文檔字符串非常簡單，就是在`函數的第一行寫下的字符串就是文檔字符`。

```python
ef fn(a: int, b: bool, c: str = 'hello') -> int:
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    return 10
```

### - 可以通過`help()`函數來查看函數

```python
help(fn)
'''
fn(a: int, b: bool, c: str = 'hello') -> int
    :param a:
    :param b:
    :param c:
    :return:

'''
```



## 13-6. 作用與命名空間

### 13-6-1. 作用域分類

#### - 全局作用域

>1. 全局作用域在程序執行時創建，在程序結束時銷毀
>
>2. 所有函數以外的區域都是全局作用域
>3. 在全局做作用域中定義的變量，都屬於全局變量，`全局變量可以在程序任何位置被訪問`

#### - 函數作用域

>1. 函數作用域在函數執行時創建，在函數結束時銷毀
>2. 函數每次調用就會產生一個新的函數作用域
>3. 在函數作用域中定義的變量，都是局部變量，它`只能在函數內部訪問`

```python
# 作用域(scope)
# 作用域是指變量生效的區域
b = 20  # 全局變量


def fn():
    a = 10  # a定義在函數內部，所以它的作用域就是函數內部，函數外部無法訪問
    print('函數內部:a=', a)
    print('函數內部:b=', b)


fn()
# print('函數外部:a=', a)
print('函數外部:b=', b)
```



### 13-6-2. 變量查找過程

#### - 當前作用域中尋找該變量，如果沒有則去上一級作用域中尋找，直到找到全局作用域

>  當我們使用變量時，會優先在當前作用域中尋找該變量，如果有則使用。如果沒有則去上一級作用域中尋找，如果有則使用。如果依然沒有則繼續去上一級作用域中尋找，依此類推。直到找到全局作用域，依然沒有找到，則會拋出異常 `NameError: name 'a' is not defined`

```python
a = 20

def fn2():
    # a = 30
    def fn3():
        # a = 40
        print('fn3中:a=', a)
    fn3()

fn2()
```



### 13-6-3. `global`關鍵字

> 在函數中為變量賦值時，默認都是為局部變量賦值，如果需要在函數內部修改全局變量，則需要使用global關鍵字，來聲明變。

```python
a = 10
b = 20
print(f'a id= {id(a):#018x}')
print(f'a= {a}, b= {b}')

def sawp_error(a, b):
    # 對局部變量做交換，無效
    a, b = b ,a
    print(f'a id= {id(a):#018x}')

def sawp_correct(aa, bb):
    global a
    global b
    a, b = bb, aa
    print(f'a id= {id(a):#018x}')

sawp_error(a, b)
print(f'a= {a}, b= {b}')

print(''.center(20,'-'))

sawp_correct(a, b)
print(f'a= {a}, b= {b}')

'''
a id= 0x00007ff854f07448
a= 10, b= 20
a id= 0x00007ff854f07588
a= 10, b= 20
--------------------
a id= 0x00007ff854f07588
a= 20, b= 10

'''
```



### 13-6-4. 命名空間(namespace)

#### - 命名空間就是一個專門用來儲存變量的字典

>
>   命名空間是指變量儲存的位置，每個變量都需要存儲到指定的命名空間中。每個作用域都會有一個它對應的命名空間。全局命名空間，用來保存全局變量。函數命名空間用來保存函數中變量，`命名空間實際上就是一個字典。是一個專門用來儲存變量的字典`。

#### - `globals()`用來獲取全局作用域的命名空間

```python
a = 20

def fn_score_glo():
    a = 10
    # globals()函數可以在任意位置獲取全局命名空間
    global_scope = globals()
    print(f'函數作用域調用globals: {global_scope}')
    print(f'函數作用域的a= {a}')
    print(f'全局作用域的a= {global_scope["a"]}')
    
fn_score_glo()
```



#### - `locals()`用來獲取當前作用域的命名空間

>1. 如果在全局作用域中調用locals()，則獲取全局命名空間
>2. 如果在函數作用域中調用locals()，則獲取函數命名空間

```python
scope = locals()    # 當前命名空間
print(f'全局作用域調用locals: {scope}')
# 向字典中添加key-value就相當於在全局中創建了一個變量(一般不建議這麼用)
scope['new_var'] = 1000
print(f'全局作用域調用(添加後)locals: {scope}')

print(''.center(20, '-'))

def fn_score_loc():
    a = 10
    scope = locals()
    # 在函數內部調用locals()會獲取到函數的命名空間
    # 可以直接操作命名空間，但不建議這麼做
    print(f'函數作用域調用locals: {scope}')

fn_score_loc()
```



## 13-7. 遞歸

### 13-7-1. 定義

#### - 簡單理解就是自己調用自己的函數

> 遞歸是解決問題的一種方式，它和循環很像。 它的整體思想是，將一個問題分解為一個一個小問題，直到問題無法分解，再去解決問題。
>
>遞歸函數的兩個要件:
>
>1. 基線條件
>
>   \- 問題可以被分解成的最小問題，當滿足基線條件時，遞歸就不在執行了。
>
>2. 遞歸條件
>
>   \- 將問題繼續分解的條件



```python
# 嘗試求n的階乘
'''
5! = 5*4! = 5*4*3! = ...
'''

def factorial(n: int):
    return 2 if n==2 else n*factorial(n-1)
```



## 13-8. 高階函數

### 13-8-1. `一等對象`的概念

>  在計算機語言理論裡，`一等對象`指的是具備以下所有特性的實體：可以被賦值給變數、可以作為參數傳遞、可以作為返回值、可以存放於資料結構中。Python 將函數、類別、模組、甚至例項都視為一等對象，讓程式具有高度的彈性與抽象能力。

#### - 能賦值給變量

#### - 能作為函數參數傳遞

#### - 能作為返回值返回

#### - 可以存放到串列、字典等資料結構中

### 13-8-2. 高階函數

#### 滿足以下任一條件

##### - 至少一個或多個函數作為參數

##### - 函數作為返回值返回

```python
# 創建一個列表
# 定義一個函數
#   可以將只指定列表中的所有偶數，保存到一個新列表中返回
# 當我們使用一個函數作為參數時，實際上就是將指定的代碼傳進了目標函數

li = range(10)

def is_even(n: int):
    return not bool(n % 2)

# python函數是一等對象
# get_by_fun是一個高階函數
def get_by_fun(datas, fun):
    li = []
    for data in datas:
        li.append(data) if fun(data) else None

    return li

print(get_by_fun(li, is_even))

# [0, 2, 4, 6, 8]
```



### 13-8-3. Python內建高階函數

#### - 匿名函數`lambda`

>  lambda函數表達式專門用來創建一些簡單的函數，它是函數創建的另一種方式。

```python
#  lambda表達式
#  語法:
#      lambda 參數列表: 返回值
fn = lambda x, y: x+y

print(fn(1, 3))
# 4
```



#### - `map(__fun, __iter)`函數

>    map()函數可以對可疊代對象中的所有元素進行指定操作，並將結果添加到一個新的可疊代對象中返回。但不會立即執行並回傳最終結果，而是`返回一個支援惰性求值（lazy）的 map 物件`。這個物件本質上是一個`一次性迭代器`，只有在遍歷或轉換為其他容器時，才會依序呼叫 `__fun` 並產生對應的結果。

```python
# 將a轉換為字符串列表 - 每個元素做類型轉換
a = [1, 2, 3]
a = map(lambda x: str(x), a)
print(f'a= {a}')
# 返回惰性求值（lazy）的 map 物件，不會馬上計算結果
# a= <map object at 0x0000017BEE237BB0>
```

##### 1. 惰性求值迭代器: 真正需要元素時才進行計算或提取

>[!NOTE]
>
> 惰性求值迭代器指的是在`真正需要元素時才進行計算或提取`，而不是一次性將所有資料載入記憶體中。它能顯著節省記憶體，並支援對無限序列或超大資料集的高效處理。

##### 2. 惰性求值迭代器特性

###### - 按需計算元素，避免一次性生成全部資料

###### - 降低峰值記憶體使用量，適合大規模或流式資料處理

###### - 能夠處理無限序列（例如自然數列、隨機數流）

###### - 在多階段資料處理管線中，各階段只在需要時觸發，提高彈性

###### - 可搭配 `for`、`next()` 使用，也能與其他迭代器串聯

```python
a = [1, 2, 3]
a = map(lambda x: str(x), a)

# 惰性求值迭代器可搭配 for、next() 使用，也能與其他迭代器串聯
print(f'next a= {next(a)}')	# next a= 1
print(f'next a= {next(a)}') # next a= 2
print(f'next a= {next(a)}') # next a= 3
# 一次性迭代器被消耗光，因此輸出空列表
print(list(a))
# []

```

#### - `reduce(__fun: (_T, _S) -> _T, __iter)`函數 

##### 1. import  functools
##### 2. 將一個可迭代物件的元素，依照使用者提供的二元函式，逐步歸約為單一結果

>需要從`functools`模組匯入。它將一個可迭代物件的元素，依照使用者提供的二元函式，逐步歸約為單一結果，常見於累加、累乘或複雜折疊操作。

```python
import functools
data = ['00', '11', '22', '33']
result = functools.reduce(lambda x, y: x+y, data)
print(f'result= {result}')
# 00112233
```



#### - `filter(__fun, __iter)`函數

##### 1. 以從序列中過濾出符合條件的元素，保存到一個新的序列中

>  filter() 是 Python 內建的高階函式，用來對可迭代物件中的每個元素套用篩選條件，僅保留回傳值為 True 的項目，並將結果以惰性迭代器形式返回。

```python
# 過濾出偶數
result = filter(lambda x: not x%2, data)
# 返回值是惰性求值迭代器
print(f'result= {result}')
# 是惰性求值迭代器可以配合for遍歷
for num in result:
    print(num, end=' ')

print()
# 0 2 4 6 8 10
```



#### - `sort(self: list, *, key, reverse)`函數

>`key`: 接收單一元素並返回用於排序比較的值的函式.
>
>`reverse`：布爾值，True 表示由大到小排序，`預設 False（由小到大,升序）.`

##### 1. 該方法用來對列表中的元素進行排序

##### 2. 預設升序排列

##### 3. 以key值對應的返回值來排序

>key需要一個函數作為參數，當設置了函數作為參數，每次都會以列表中的一個元素作為參數來調用函數，並使用函數的返回值大小來進行排序.

```python
# 以字符串長度排序
l = ['bb', 'aaaa', 'c', 'ddddddd', 'fff']
l.sort(key=len)
print(l)
```



#### - `sorted(list, *, key, reverse)`函數

 >  這個函數和sort()用來基本一致，但是sorted()可以對任意序列進行排序，並且使用sorted()排序不會影響原來的對象，而是返回一個新的對象。

##### - 和sort()區別，返回一個新的對象

```python
# 轉整數值後排序
l = [2, 5, '1', 3, '6', '4']
print('排序前l:', l)
ln = sorted(l, key=int)
print('排序後l:', l)
print('ln:', ln)
```





### 13-8-4. 閉包及裝飾器

#### - 閉包概念

#####  將函數作為返回值返回，這種高階函數我們也稱為閉包

>  將函數作為返回值返回，也是一種高階函數，這種高階函數我們也稱為閉包，通過閉包可以創建一些只有當前函數能訪問的變量，可以將一些私有的數據藏到閉包中.



#### - 閉包的條件

##### 1. 函數嵌套

##### 2. 將內部函數作為外部函數的返回值

##### 3. 內部函數使用外部函數中的變量

```python
def make_average():
    nums = []
    # 創建一個函數，用來算平均值
    def average(n):
        # 將n添加到列表中
        nums.append(n)
        # 求平均值
        return sum(nums)/len(nums)

    return average


average = make_average()
print(average(10))
print(average(10))
print(average(30))

```



#### - 裝飾器

>  裝飾器是函式式編程中的一種高階函式，用於`在不修改原函式程式碼`的前提下，動態地為函式或方法添加額外功能。簡言之，裝飾器會接受一個函式並返回一個「包裹後」的函式，使得原函式行為被擴充或改變.



##### 1. 開閉原則(OCP):　開放對程序的擴展，關閉對程序的修改

>　　希望函數可以在計算前，打印開始計算，計算結束後打印計算完畢，，我們可以直接通過修改函數中的代碼來ｊ完＞成這個需求，但是會產生以下一些問題.
>1. 如果要修改的函數過多，修改起來會比較麻煩
>2. 並且不方便後期維護
>3. 並且這樣會違反開閉原則(OCP)



##### 2. 裝飾器的核心條件

###### - 接受一個函式作為參數

###### - 返回一個新的函式作為結果

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # 裝飾前邏輯
        result = func(*args, **kwargs)
        # 裝飾後邏輯
        return result
    return wrapper

@decorator
def original_function(...):
    ...
```


##### 3. 通過@裝飾器，來裝飾當前的函數

###### 可以同時為一個函數指定多個裝飾器，這樣函數將會依照由內向外的順序被裝飾

```python
def begin_end(old):
    """
        用來對其他函數進行擴展，使其他函數可以在執行前打印函數開始執行，在函數結束後打印函數執行結束
        參數:
            old 要擴展的函數對象
    """
    # 創建一新的函數
    def new_function(*args, **kwargs):
        print('函數開始執行~~~')
        # 調用被擴展的函數
        r = old(*args, **kwargs)
        print('函數執行結束~~~')
        return r

    # 返回新函數
    return new_function

def fn3(old):
    """
        用來對其他函數進行擴展，使其他函數可以在執行前打印函數開始執行，在函數結束後打印函數執行結束
        參數:
            old 要擴展的函數對象
    """
    # 創建一新的函數
    def new_function(*args, **kwargs):
        print('fn3裝飾器~~~')
        # 調用被擴展的函數
        r = old(*args, **kwargs)
        print('fn3裝飾器~~~')
        return r

    # 返回新函數
    return new_function

f = begin_end(mul)
# f2 = begin_end()
# print(f)
# print(f2)
print(f(5, 3))

# 向begin_end()這種函數我們就稱之為裝飾器
#  通過裝飾器，可以在不修改原函數的情況下，對函數進行擴展
#  在開發中，我們都是通過裝飾器來擴展函數功能
@begin_end
@fn3
def say_hello():
    print('大家好~~~')

say_hello()
```



##### 4. 帶參數的裝飾器

###### - 帶參數裝飾器其實是「能接受額外參數的裝飾器工廠」，`本質上是多一層函式包裝`

>  帶參數裝飾器其實是「能接受額外參數的裝飾器工廠」，本質上是多一層函式包裝。從外到內依序分為：
>
>1. 工廠函式（Decorator Factory）：接收使用者傳入的參數，並回傳真正的裝飾器.
>2. 裝飾器函式（Decorator）：接收被裝飾的目標函式 `func`，並定義如何包裹它.
>3. 包裹函式（Wrapper）：取代原函式執行，並在呼叫前後插入額外行為.



###### - 裝飾後調用原函式，利用 `__wrapped__`屬性

>  當你的裝飾器使用了 `functools.wraps`，wrapper 物件會自動帶上` __wrapped__ `屬性，指向被包裹的原函式。

```python
from functools import wraps

def deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper

@deco
def greet(name):
    print("Hello", name)

# 一般呼叫，會執行 wrapper
greet("Alice")
# before
# Hello Alice
# after

# 呼叫原始函式
greet.__wrapped__("Alice")
# Hello Alice

```



```python
# 應用情境
'''
假設我們已經定義了一個函數task，這個函數接受一個變量並返回一個執行結果
ex: 自動測試中給定的測試參數，返回一個測試結果

利用裝飾器來達到多次執行的多功能，但我們又希望每次執行的輸入參數是變動的
*使用帶參數的裝飾器

ex:
run1 param1-1,param1-2
run2 param2-1,param2-2
run3 param3-1,param3-2
run4 param4-1,param4-2
run5 param5-1,param5-2

'''
def multi_run_script(runs: list):
    def multi_run(task):
        def multi_run_task(*args, **kwargs):
            result = []
            for i in range(len(runs)):
                # 將多次執行結果返回到一個列表之中
                result.append(task(*runs[i]))

            return result

        return multi_run_task

    return multi_run


from functools import wraps

def multi_run_5times(task):
    @wraps(task)
    def multi_run_task(*args, **kwargs):
        result = []
        for i in range(5):
            # 將多次執行結果返回到一個列表之中
            result.append(task(*args))

        return result

    return multi_run_task


@multi_run_5times
# @multi_run_script([('1-1', '1-2'), ('2-1', '2-2'), ('3-1', '3-2')])
def task(*test_params):

    test_results =  *test_params, random.randint(0, 100), random.randint(10, 20)
    # print(test_results)
    return test_results

# 執行1次task的結果
print(task.__wrapped__('1-1', '1-2'))
# ('1-1', '1-2', 65, 14)
# 執行五次task的結果
print(task('1-1', '1-2'))

# 執行多次task的結果
# 動態調用方式
runs = ((str(i)+'-1', str(i)+'-2')for i in range(1, 4))
print(multi_run_script(list(runs))(task.__wrapped__)())
# [('1-1', '1-2', 31, 17), ('2-1', '2-2', 90, 14), ('3-1', '3-2', 81, 17)]
```



<span alt="solid">範例: 13_函數</span>



---

# 14. 類

## 14-1. 類的簡介

### 14-1-1. 對象: 對象是內存中專門用來存儲數據的一塊區域

### 14-1-2. 對象組成: `id`/`type`/`value`

>對象有三部分組成
> 1. 對象的標誌(`id`)
> 2. 對象的類型(`type`)
> 3. 對象的值(`value`)
>

### 14-1-3. 面向對像（Object-Oriented Programming)

>  面向對象（Object-Oriented Programming, OOP）是一種程式設計思想，核心在於「以物件為中心」來建構程式，而不是單純依照步驟或流程來撰寫。這種方法更貼近人類理解世界的方式，也更有利於大型系統的設計與維護。 所謂的面向對象的語言，簡單理解就是語言中的所有操作都是通過對象來進行的。

 

+ 面向過程的編程語言: 面向過程語言指的是將我們的程序的邏輯分解為一個一個步驟，通過對每個步驟的抽象，來完成程序。

>[!NOTE]
>
>例子: 
>
>- 孩子上學
>1. 媽媽起床
>2. 媽媽上廁所
>3. 媽媽洗漱
>4. 媽媽做早飯
>5. 媽媽叫孩子起床
>6. 孩子上廁所
>7. 孩子洗漱
>8. 孩子吃早餐
>9. 孩子背著書包上學
>
>  面向過程的編程思想將一個一個功能分解為一個一個小步驟，我們通過完成一個一個小步驟來完成一個程序。這種編程方式，符合我們人類的思維，編寫起來相對比較簡單，但這種方式編寫的代碼往往只適用一個功能，如果要在實現別的功能，往往要在重新編寫代碼，可複用性較低，並且難維護。



+ 面向對象的編程語言:　面向對象的編程語言關注的是對象，而不關注過程。對於面向對象語言來說，一切都是對象。

>[!NOTE]
>
>例子:
>- 孩他媽起床叫孩子上
>
>  面向對象的編程思想，將所有的功能保存到對應的對象中。比如，媽媽功能保存到媽媽對象中，孩子功能保存到孩子對象中，要使用某個功能，直接找到對應的對象即可。
>
>  這種方式編寫的代碼，比較容易閱讀，並且比較容易維護，容易複用，但這種編寫方式，不太符合常規思維，編寫起來稍微麻煩一點。



+ 與面向過程的比較

| 面向過程（Procedure-Oriented） | 面向對象（Object-Oriented）        |
| ------------------------------ | ---------------------------------- |
| 以函數為中心，強調步驟與流程   | 以對象為中心，強調資料與行為的整合 |
| 程式結構較為扁平，耦合度高     | 程式結構清晰，低耦合高內聚         |
| 適合小型、性能敏感的系統       | 適合大型、複雜、可維護性高的系統   |





## 14-2. 面向對象的核心概念

| 概念                  | 說明                                                         |
| --------------------- | ------------------------------------------------------------ |
| 類（Class）           | 對一類事物的抽象描述，定義了屬性（資料）與方法（行為）       |
| 物件（Object）        | 類的具體實例，擁有類所定義的屬性與方法                       |
| 封裝（Encapsulation） | 將資料與操作封裝在物件中，對外只暴露必要的介面，隱藏內部實作細節 |
| 繼承（Inheritance）   | 子類可以繼承父類的屬性與方法，實現程式碼重用與擴展           |
| 多型（Polymorphism）  | 同一方法在不同物件上可有不同表現，提升系統的靈活性與可擴展性 |



### 14-2-1. 類定義`class`

#### 1. 創建類

##### - `isinstance(obj, class)`: 檢查一個對象是否是一個類的實例

```python
# 定義一個簡單的類
# 使用class關鍵字來定義類，語法和函數很像
# 語法:
#   class 類名([父類]):
#       代碼塊
class MyClass():
    pass

# 使用MyClass來創建一個對象
# 使用類來創建對象，就像調用一個函數一樣
mc = MyClass()    # mc就是通過MyClass創建的對象，mc就是MyClass的實例
mc2 = MyClass()
mc3 = MyClass()
mc4 = MyClass()
# mc mc2 mc3 mc4都是MyClass的實例，他們都是一類對象
print(mc)

# isinstance()用來檢查一個對象是否是一個類的實例
print(isinstance(mc, MyClass))
```



##### - python中可以動態為實例添加`屬性`

>   通過MyClass這個類創建對象都是一個空對象，也就是對象中實際上什麼都沒有，就相當於是一個空盒子。可以向對象中添加變量，對象中的變量我們稱為`屬性`。
>
> 語法: `對象.屬性名 = 屬性值`

```python
class MyClass():
    pass

mc = MyClass()
# 語法: 對象.屬性名 = 屬性值
mc.name = '孫悟空'
print(mc.name)
```



#### 2. 定義類

>類的定義: 
>
>1. 類和對象都是對現實生活中或程序中的內容進行抽象。
>2. 實際上所有事物都由兩部份組成
>     \- 數據(屬性)
>     \- 行為(方法) 

```python
# 嘗試定義一個表示人的類
class Person:
    # 在類的代碼塊中，我們可以定義變量和函數
    # 在類中我們定義的變量，將會成為所有實例的公共屬性
    # 所有實例都可以訪問這些變量
    name = 'swk'    # 公共屬性，所以有的實例都可以訪問

    # 在類中也可以定義函數，類中定義的函數，我們稱為方法
    # 這些方法可以通過該類的所有實例來訪問
    def say_hello(self):
        # *方法每次調用時，解析器都會自動傳遞第一個實參
        # print(a)
        #   第一個參數，就是調用方法的對象本身
        #   如果是p1調的，則第一個參數就是p1對象
        #   如果是p2調的，則第一個參數就是p2對象
        # 一般我們都會將這個參數命名為self

        # say_hello()這個方法，可以顯示如下格式數據:
        # 你好! 我是xxx
        # 在方法中不能直接訪問類中的屬性
        # print(f'你好!我是{name}')
        print(f'你好!我是{self.name}')
```

##### - `self`說明

###### `當前類的實例本身`

>  在 Python 類中，是一個非常關鍵的參數，它代表`當前類的實例本身`。當你在類中定義方法時， 讓你能夠訪問該實例的屬性與其他方法。

+ self 的用途與意義

   \- 是每個實例方法的第一個參數（雖然呼叫時不需手動傳入）。

   \- 它指向該方法所屬的實例，讓你能操作該對象的屬性與行為。

   \- 類似於其他語言中的`this`關鍵字。



##### - `類屬性`

>  在類的代碼塊中，我們可以定義變量。變量會成為該類實例的公共屬性，該類所有的實例都可以通過 `對象[類名].屬性名`來訪問這個公共屬性。

+ 屬性查找過程

    當我們調用一個對象的屬性時，解析器會先在當前對象中尋找是否含有該屬性，如果有，則直接返回當前對象的屬性值，如果沒有，則去當前對象的類對象中查找，如果有則返回類對象的屬性值，如果沒有則報錯。

  

##### - `方法`

>  類的代碼塊中，我們可以定義函數。函數會成為該類實例的公共方法，所有該類的實例都可以通過`對象.方法名()` 來調用這個方法。



```python
# 創建Person的實例
p1 = Person()
p1.name = '豬八戒'
# 調用方法，對象.方法名()
# 方法調用和函數調用區別
# 如果是函數調用，則調用時傳幾個參數，就會有幾個實參
# 如果是方法調用，默認會傳遞一個參數(self)，所以方法中至少要定義一個形參
p1.say_hello()
print(p1.name)
p2 = Person()
print(p2.name)

'''
你好!我是豬八戒
豬八戒
swk
'''
```

#### 3. 對象初始化

##### - 魔術(特殊)方法

###### 特殊方法都是以`__`開頭，`__`。特殊方法將會在特殊時刻自動調用(不要嘗試去調用特殊方法)

> 在Python類中，特殊方法是以`雙下劃線開頭與結尾的方法`，讓自訂類別可與內建語法與運算符無縫整合，而不需手動呼叫這些方法。


| 分類             | 方法示例                                                     | 功能說明                                       |
| ---------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| 物件生命週期     | `__new__`, `__init__`, `__del__`, `__init_subclass__`        | 控制實例建立、初始化、銷毀與子類化             |         |
| 比較運算         | `__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__ne__`   | 支援等於、大於、小於等比較操作                 |
| 容器協議         | `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__iter__`, `__next__`, `__contains__` | 令物件支援長度查詢、索引、切片、迭代、成員判斷 |
| 運算符重載       | `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__and__`, `__or__`, `__xor__`, `__lshift__`, … | 自訂算術與位元運算行為                         |
| 字串與格式化     | `__str__`, `__repr__`, `__format__`, `__bytes__`             | 控制物件輸出字串、調試表示與格式化             |



##### - 構造與析構

###### `__init__()`對象創建以後立即執行

###### `__del__()` 對象創建銷毀後立即執行

```python
class Person:
    # 特殊方法都是以__開頭，__結尾
    # 特殊方法我們不需要自己調用，不要嘗試去調用特殊方法
    # 特殊方法將會在特殊時刻自動調用
    # init會在對象創建以後立即執行
    # init可以用來向新創建的對象添加初始化屬性
    # 調用類創建對象時，類後面的所有參數都會依序傳遞到__init__()中
    def __init__(self, name):
        # 通過self向新創建的對象添加屬性
        self.name = name

    def __del__(self):
        # 對象回收時會自動調用
        print('對象銷毀')    

    def say_hello(self):
        print(f'大家好!我是{self.name}')

# 對象創建時會自動調用__inti__()方法
p1 = Person('孫悟空')
p1.say_hello()
# 對象回收時會自動調用__del__()方法
p1 = None

'''
大家好!我是孫悟空
對象銷毀
'''
```


#### 4.  類的基本結構

```python
# 類的基本結構
class 類名([父類]):
	# 公共屬性
	# 對象的初始方法
	def __init__(self,...):
		...
	def method1(self,...):
		...
	def method2(self,...):
		...
```



### 14-2-2. 封裝（Encapsulation）

#### 1. 什麼是封裝: `隱藏實作細節，僅暴露必要介面`

>  在程式設計中，封裝（Encapsulation）指的是將物件的屬性（資料）和方法（行為）打包在一起，並對外隱藏實作細節。外部程式只能透過一組公開的介面（方法或屬性存取器）來讀取或修改內部狀態，避免誤用或破壞物件不變性。

+ 如何隱藏一個對象的屬性?

   \- 將對象的屬性名，修改為一個外部不知道的名字。

+ 如何獲取(修改)對象中的屬性?

   \- 提供一個getter和setter方法，使外部可以訪問到該屬性。

   \- getter獲取對象中的屬性名(get_屬性名)。

   \- setter用來設置對象的指定屬性(set_屬性名)。

#####  - 隱藏了屬性名，使調用者無法隨意更改對象中的屬性。

#####  - 增加了getter和setter方法，可以很好的控制屬性是否是只讀的。

>[!NOTE]
>
>1. 如果希望屬性是只讀的，則可以直接去掉setter。
>2. 如果不希望屬性被外部訪問，則可以直接去掉getter。

##### - 使用setter方法設置屬性，可以增加數據的校驗，確保數據值是否是正確的。

##### - 可以在讀取屬性和設置屬性的同時進行其他的處理。

```python
class Dog:
    """
        表示狗的類
    """
    def __init__(self, name, age):
        self.hidden_name = name
        self.hidden_age = age

    def say_hello(self):
        print('大家好，我是%s' % self.hidden_name)

    def get_name(self):
        """
            用來獲取對象的name屬性
        """
        # print('用戶讀取了屬性')
        return self.hidden_name

    def set_name(self, name):
        # print('用戶修改了屬性')
        self.hidden_name = name

    def get_age(self):
        return self.hidden_age

    def set_age(self, age):
        if age > 0:
            self.hidden_age = age


d = Dog('旺財', 3)
d.say_hello()
# 通過setter方法來修改name屬性
d.set_name('小黑')
d.say_hello()
```



#### 2. Python封裝方式

| 屬性類型 | 命名方式      | 存取限制       | 說明                                   |
| -------- | ------------- | -------------- | -------------------------------------- |
| 公開屬性 | `self.name`   | 無限制         | 可自由存取                             |
| 保護屬性 | `self._name`  | 建議勿直接存取 | 約定俗成，非強制                       |
| 私有屬性 | `self.__name` | 嚴格限制       | Python 會進行名稱改寫（name mangling） |

##### - 屬性封裝`_屬性名`(保護),`__屬性名`(私有)

##### - 函數封裝`_函數名`(保護),`__函數名`(私有)

##### - 私有的名稱改寫規則 `_類名__函數或屬性名`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        # 保護屬性
        self._money = 0
        # 私有屬性
        self.__age = age

    def __get_age(self):
        return self.__age

    def _get_age(self):
        return self.__age



p = Person('Amy', 20)
# 保護方式實際上還是可以存取。但不建議這麼做
p._money = 100

print(f'Amy有{p._money}塊')

# 無法訪問私有屬性， __age 變為 _Person__age
# AttributeError: 'Person' object has no attribute '__age'
# 錯誤訪問方式
# print(f'Amy目前{p.__age}歲')
print(f'Amy目前{p._Person__age}歲')

# 注意以下範例
# 此為添加__age屬性，並非修改_Person__age屬性
p.__age = 30
print(f'Amy目前{p._Person__age}歲')
print(f'Amy目前{p.__age}歲')


# 保護函數，依然可以訪問
print(f'Amy目前{p._get_age()}歲')

# 私有函數，無法訪問 __get_age() 變為 _Person__get_age
# AttributeError: 'Person' object has no attribute '__get_age'. Did you mean: '_get_age'?
print(f'Amy目前{p._Person__get_age()}歲')
```



#### 3. 使用`@property`裝飾器實現封裝(推薦使用)

>使用 @property，我們可將原本需要呼叫的方法，變成像存取屬性一樣自然地讀寫。這樣一來，內部仍能保有私有屬性與驗證邏輯，同時對外提供簡潔的介面。

+ 與傳統 getter/setter 的比較

  | 特性         | 傳統方法         | `@property` 寫法     |
  | ------------ | ---------------- | -------------------- |
  | 呼叫方式     | `p.get_age()`    | `p.age`              |
  | 設定方式     | `p.set_age(25)`  | `p.age = 25`         |
  | 介面簡潔度   | 較冗長           | 更直觀、像屬性存取   |
  | 强制驗證邏輯 | 需在 setter 寫入 | 同樣可在 setter 執行 |



```python
class Person:
    def __init__(self, name):
        self._name = name

    # property裝飾器，用來將一個get方法，轉換為對象屬性
    # 添加property裝飾器以後，我們就可以象調用屬性一樣使用get方法
    # 使用property裝飾器的方法，必須和屬性名一致
    @property
    def name(self):
        print('get方法執行了')
        return self._name

    # setter方法的裝飾器: @屬性名.setter
    @name.setter
    def name(self, name):
        print('setter方法執行了')
        self._name = name

p = Person('孫悟空')
# print(p.name())
p.name = '豬八戒'
print(p.name)
```



### 14-2-3. 繼承（Inheritance）

#### 1. 什麼是繼承: 繼承讓子類別可以重用並擴展父類別的屬性和方法

>  繼承允許新定義的子類別（subclass）自動取得父類別（base class）的屬性和方法。這種機制能`促進程式碼重用`與`類別間的關係建模`。

+ 範例: 定義一個動物類及狗類。其中狗類繼承自動物類。(由動物類派生狗類)。

##### - `isinstance()`: 檢查一個對象是否是一個類的實例

##### - `issubclass()`: 檢查一個對象是否是一個類的子類

```python
# 繼承
# 定義一個類Animal(動物)
#   這個類中需要兩個方法: run() sleep()

class Animal:
    def run(self):
        print('動物會跑')

    def sleep(self):
        print('動物睡覺')

# 定義一個狗類
#   這個類中需要三個方法: run() sleep()  bark()
# 有一個類，能實現我們大部分功能，但不能實現全部功能
# 如何能讓這個類來實現全部的功能?
#   1. 直接修改這個類，在類中添加我們需要的功能
#      - 修改起來會比較麻煩，並且會違反OCP原則
#   2. 直接創建一個新的類
#      - 創建一個新的類比較麻煩，並且需要進行大量的複製貼上，會出現大量的重複性大代碼
#   3. 直接從Animal類中來繼承它的屬性和方法
#      - 繼承是面向對象三大特性之一
#      - 通過繼承我們可以使一個類獲取到其他類中的屬性和方法
#      - 在定義類時，可以在類名後的括號中指定當前類的父類(超類、基類、super)
#          子類(衍生類)可以直接繼承父類中的所有屬性和方法
#
#  通過繼承可以直接讓子類獲取到父類中的屬性和方法，避免編寫重複性代碼，並符合OCP原則
#    所以我們經常需要通過繼承來對一個類進行擴展

class Dog(Animal):
    def bark(self):
        print('狗在嚎叫~~')

d = Dog()
d.bark()
d.run()

# 在創建類時，如果省略了父類，則默認父類為object
#  object是所有類的父類，所有類都繼承自object

# isinstance()檢查一個對象是否是一個類的實例
#   如果這個類是這個對象的父類，也會返回True
#   所有對象都是object的實例
print(isinstance(d, Dog))
print(isinstance(d, object))

# issubclass()檢查一個類是否是另一個類的子類
print(issubclass(Dog, Animal))
print(isinstance(d, Animal))
```



#### 2. 繼承的語法

##### - 單一繼承

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    pass

c = Child()
c.greet()  # 輸出：Hello from Parent
```

>1. 告子類別只需在類名後面括號內指定父類別名稱。
>2. 子類別如果不做覆寫，就會直接使用父類別的方法。

##### - 方法覆寫（Override）

>  若子類別需要修改父類別的方法，只要在子類別中重新定義同名方法即可。

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

c = Child()
c.greet()  # 輸出：Hello from Child

```

>[!NOTE]
>
>  當調用一個對象的方法時，會優先去當前對象中尋找是否具有該方法，如果有則直接使用，如果沒有會去當前對象的父類中尋找，如果父類中有該方法，則直接調用父類中的方法，如果沒有，則去父類的父類中尋找，以此類推，直到找到object為止，如果依然沒找到則報錯。



##### - `super()`呼叫父類別方法

>1. 父類中的所有方法都會被子類繼承，包含特殊方法。
>2. 當子類中有增加的屬性時，構造函數需要增加參數，這時可以重寫`__init__()`，但對於父類的初始，需要使用`super()`來調用父類的構造。
>3. 也可以透過`super()`來調用父類的方法。
>

```python
class Aniaml:
    def __init__(self, name):
        self._name = name

    def run(self):
        print('動物會跑~~~')

    def sleep(self):
        print('動物睡覺~~~')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


# 父類中的所有方法都會被子類繼承，包刮特殊方法，也可以重寫特殊方法

class Dog(Aniaml):
    def __init__(self, name, age):
        # 希望可以直接調用父類的__init__來初始化父類中定義的屬性
        # super()可以用獲取當前類的父類
        #  並且通過super()返回對象來調用父類方法，不需要傳遞self
        super(Dog, self).__init__(name)
        # super().__init__(name)
        # Aniaml.__init__(self, name)
        self._age = age

    def bark(self):
        print('汪汪汪~~~')

    def run(self):
        print('狗跑')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

        
d = Dog('哈士奇', 6)
print(d.name)
print(d.age)
```

>[!NOTE]
>1. 繼承Aniaml構造函數只需要一個name作為參數，如果Dog類多了一個age參數，在初始化階段會報錯
>     --> 解決方式重寫子類的`__init__()`並新增一個參數
>2. 為了保留為父類的邏輯需要調用父類的構造，如何調用父類的方法
>     --> 使用`super()`來調用父類方法
>



##### - 多重繼承

>  在Python中是支持多重繼承的，也就是我們可以為一個類同時指定多個父類。可以在類名中的()添加多個類，來實現多重繼承
>多重繼承，會使子類同時擁有多個父類，並且會獲取到父類中所有方法。在開發中沒有特殊情況，應該盡量避免使用多重繼承，因為多重繼承會讓代碼過於複雜。

###### `__bases__`: 這個屬性可以用來獲取當前類的所有父類

```python
class A(object):
    def test(self):
        print('AAA')

    def test2(self):
        print('A_BBB')

class B(object):
    def test2(self):
        print('BBB')

# C(A, B) 、 C(B, A)
class C(A, B):
    def test3(self):
        print('CCC')

# __bases__ 這個屬性可以用來獲取當前類的所有父類
c = C()
c.test2()
print(C.__bases__)
```

>[!NOTE]
>  如果多個父類中有同名的方法，則會在第一個父類中尋找，如果有則使用,如果沒有則會往下面的父類尋找，依此類推，如果都沒找到則會報錯。




### 14-2-4. 多態（Polymorphism）

#### 1. 什麼是多態: 多態是指在相同介面下，不同類別的物件可以各自以自己的方式回應呼叫的能力

>  多態性允許在相同介面（方法名稱）下，對不同類別的物件執行各自適切的行為。這能強化程式碼的靈活度與可擴充性，減少大量的條件分支判斷。

```python
# 定義兩個類
class A:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class B:
    def __init__(self, name):
        self._name = name

    def __len__(self):
        return 10

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

class C:
    pass
a = A('孫悟空')
b = B('豬八戒')
c = C()

# 定義一個函數
# 對於say_hello()這個函數來說，只要對象中存在name屬性，它就可以作為實參傳遞
#  這個函數並不會考慮對象的類型，只要有name屬性即可
def say_hello(obj):
    print('你好 %s' % obj.name)

    
say_hello(a)
say_hello(b)

# len()
# 之所以一個對象能通過len()來獲取長度，是因為對象中具有一個特殊方法__len__
# 換句話說，只要對象中具有__len__這個特殊方法，就可以通過len()來獲取長度

l = [1, 2, 3]
s = 'hello'
print(len(l))
print(len(s))
print(len(b))

```



## 14-3. 類的屬性與方法

### 14-3-1. 類屬性與實例屬性

>      在 Python 中，`類屬性（Class Attributes)` 是屬於類本身的變數，而不是某個特定實例。這些屬性會被所有實例共享，與`實例屬性（Instance Attributes)`不同)。

#### - 實例屬性只能通過實例訪問，無法通過類訪問實例屬性

#### - 類屬性可以被類及實例訪問

#### - 類屬性只能被類修改，無法通過實例修改。(通過實例修改會建立一個新的實例屬性，遮蔽原本的類屬性)

+ 類屬性 vs 實例屬性

| 屬性類型 | 定義位置                      | 是否共享 | 訪問方式                             |
| -------- | ----------------------------- | -------- | ------------------------------------ |
| 類屬性   | 類內部、方法外部              | ✅ 是     | `ClassName.attr`) 或 `instance.attr` |
| 實例屬性 | 類方法內部，通常在 `__init__` | ❌ 否     | `self.attr`                          |

```python
class A(object):

    # 類屬性
    # 實例屬性

    # 類屬性，直接在類中定義的屬性是類屬性
    # 類屬性可以通過類和類的實例訪問到
    # 但是類屬性只能通過類對象來修改，無法通過實例對象來修改
    count = 0

    def __init__(self):
        # 實例屬性，通過實例對象添加的屬性屬於實例屬性
        # 實例屬性只能通過實例對象訪問和修改，類對象無法訪問修改
        self.name = '孫悟空'
        
a = A()
# 實例屬性，通過實例對象添加的屬性屬於實例屬性
a.count = 1
A.count = 100
print(a.count, ' ', id(a.count))
print(A.count, ' ', id(A.count))

'''
1   140711216313128
100   140711216316296
'''
```

>[!NOTE]
>
>1. 若透過 [`instance.attr`](https://instance.attr)` = value` 修改類屬性，會建立一個新的實例屬性，遮蔽原本的類屬性。(`無法通過實例修改類屬性`)
>
>2. 類屬性適合儲存所有實例共通的資料，例如常數、設定值等。

### 14-3-2. 類方法與實例方法

>  實例方法只能透過實例呼叫，第一個參數是`self` ，可以存取該實例的屬性與類別屬性。類方法使用`@classmethod`裝飾，第一個參數是`cls`，可透過類別或實例呼叫，但只能存取或修改類別屬性。

#### - 通過實例調用實例方法時，第一個`self`參數為自動傳遞

#### - 通過類調用實例方法時，第一個`self`參數不會自動傳遞，需要自行傳遞(一般不這麼用)

#### - 通過類或實例調用類方法時，第一個`cls`參數會自動傳遞

#### - 可以通過實例調用類方法來修改類屬性，間接完成實例修改類屬性的功能。



```python
class A(object):
    # 實例方法
    # 類方法
    # 靜態方法
    count = 0

    def __init__(self):
        pass

    # 實例方法
    #  在類中定義，以self為第一個參數的方法都是實例方法
    # 實例方法在調用時，Python會將調用對象作為self傳入
    # 實例方法可以通過實例和類去調用
    #   當通過實例去調用時，會自動將當前調用的對象作self傳入
    #   當通過類去調用時，不會自動傳遞self，此時我們必須手動傳遞self
    def test(self):
        print('這是test方法~~~', self)

    # 類方法
    # 在類內部使用 @classmethod 來修飾的方法屬於類方法
    # 類方法的第一個參數是cls，也會被自動傳遞，cls就是當前的類對象
    #  類方法和實例方法的區別，實例方法第一個參數是self，而類方法第一個參數是cls
    #  類方法可以通過類去調用，也可以通過實例調用，沒有區別
    @classmethod
    def test2(cls):
        cls.count = temp
        print('這是test2方法~~', cls)
        
a = A()
# a.test()等價於A.test(a)
a.test()
A.test(a)

A.test2(0)
# 我們知道通過實例不能直接修改類屬性，但可以間接透過調用類方法來修改類屬性
a.test2(1000)
print(A.count)

```



### 14-3-3. `@classmethod`與@`staticmethod`差異

#### - `@staticmethod`: 定義不依賴於類別或實例的靜態方法，不接收 `self` 或 `cls`，更像是在類內部定義的普通函式。

#### - `@classmethod`: 定義綁定到類別的方法，第一個參數是 `cls`，可透過它訪問或修改類別層級的屬性，並常用於工廠方法或管理共享狀態。

```python
class A(object):
    def __init__(self):
     	pass
    
    # 靜態方法
    # 在類中使用 @staticmethod 來修飾的方法屬於靜態方法
    # 靜態方法不需要指定任何默認參數，靜態方法可以通過類和實例調用
    # 靜態方法基本上是一個和當前類無關的方法，它只是保存到當前類中的函數
    # 靜態方法一般都是一些工具方法，和當前類無關
    @staticmethod
    def test3():
        print('這是test3方法')

a = A()

A.test3()
a.test3()
```



## 14-4. 垃圾回收

>    就像我們生活中會產生垃圾一樣，程序在運行過程當中也會產生垃圾，程序運行當中的垃圾會影響到程序運行的效能，所以這些垃圾必須被即時清理，沒有用的東西就是垃圾，在程序中沒有被引用的對象就是垃圾，這種圾垃對象過多以後會影響到程序的運行效能，所以我們必須進行即時的垃圾回收，所謂的垃圾回收就是將垃圾對象從內存中刪除，在Python中有自動的圾垃回收機制，它將會自動將沒有被引用的對象刪除，所以我們不用手動處理垃圾回收。

```python
class A:
    def __init__(self):
        self.name = 'A類'

    # del是一個特殊方法，它會在對象被垃圾回收前調用
    def __del__(self):
        print('A()對象被刪除了~~~~', self)


a = A()

# b = a

# 將a設置為了None，此時沒有任何變量對A()對象進行引用，它就變成了垃圾
a = None

input('回車鍵退出...')
```



## 14-5. 特殊方法補充

### 14-5-1. 實例化

#### - `__new__(cls, *args, **kwargs)`: 創建實例(靜態方法，必須返回實例)

>  `__new__` 是一個`靜態方法`，用於`創建並返回類的新實例`，並在 `__init__` 之前執行。它接收一個參數 `cls`，`必須返回一個該類或其子類的實例`。如果返回其他類型或 `None`，`__init__` 就不會被執行。

#### - `__init__(self, *args, **kwargs)`: 實例初始

#### - `__del__(self)`: 實例的銷毀

```python
class Person:
    def __new__(cls, *args, **kwargs):
        print('cls= ',cls)
        print('args= ', args)
        print('kwargs ', kwargs)
        print('__new__被調用了')
        # __new__必須返回一個實例，反__init__不會被調用
        # 如何創建實例
        # 1. 不可以自己創建，會造成遞規創建
        # 2. 通過父類的實例方法__new__來創建並返回實例，__new__是一個靜態方法必需手動傳參
        return super().__new__(cls)
        # 錯誤: RecursionError: maximum recursion depth exceeded while calling a Python object
        # return cls(*args, **kwargs)

    def __init__(self, name, age=18):
        # 在 __new__ 返回後被調用
        print('__init__被調用了')
        self.name = name
        self.age = age


p1 = Person('Jeff', age=20)
print(p1)

'''
cls=  <class '__main__.Person'>
args=  ('Jeff',)
kwargs  {'age': 20}
__new__被調用了
__init__被調用了
<__main__.Person object at 0x000001546D09E050>
'''
```



### 14-5-2. 可視化

#### - `__str__`

>   `str()`函數、`format()`函數、`print()`函數調用。需要返回對象的字符串表達。如果沒有定義就會去調用`__repr__`返回字符串表達。如果`__repr__`沒有定義，就返回對象的內存地址信息。

#### - `__repr__`

>  內建函數`repr()`對一個對象獲取字符串表達。調用`__repr__`方法返回自字符串表達。如果`__repr__`沒有定義，就直接返回對對象地址信息。

#### - `__bytes__`

>  `bytes()`函數調用，返回一的對象的bytes表達，即返回bytes對象。

```python
import json


class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def __str__(self):
        return f'[__str__] name= {self.name}, age= {self.age}'

    def __repr__(self):
        return f'[__repr__] name= {self.name}, age= {self.age}'

    def __bytes__(self):
        return json.dumps(self.__dict__).encode()

p1 = Person('Jeff', age=20)

print(p1)
print(str(p1))
print(f'{p1}')

print([p1, p1]) # []使用__str__，但其內部使用__repr__
print([str(p1)]) # []使用__str__，其中元素使用str()也使用__str__

print(bytes(p1))

'''
[__str__] name= Jeff, age= 20
[__str__] name= Jeff, age= 20
[__str__] name= Jeff, age= 20
[[__repr__] name= Jeff, age= 20, [__repr__] name= Jeff, age= 20]
['[__str__] name= Jeff, age= 20']
b'{"name": "Jeff", "age": 20}'

'''
```



### 14-5-3. `hash`

#### - `__hash__`

>  內建函數`hash()`調用的返回值，`返回一個整數`，如果定義這個方法該類的實例就可以hash。

>[!NOTE]
> set去重原理
> step1. 第一步必須求hash，hash衝突了才需要去重
> step2. 第二步 去重 比較內容

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        # 1. __hash__返回值必須為整型
        return 100
        # return  hash(self.name)

    def __repr__(self):
        return self.name

    # 運算符重載
    def __eq__(self, other):
        return self.name == other.name


print(hash(Person))
# print(hash(Person('Tom')))
# print(hash(Person('Jeff')))

tom1 = Person('Tom')
tom2 = Person('Tom')
print(f'tom1 hash= {hash(tom1)}')
print(f'tom2 hash= {hash(tom2)}')

print([tom1, tom2]) # [Tom, Tom]
print((tom1, tom2)) # (Tom, Tom)
print({'Tom', 'Tom'}) # {Tom}
'''
hash地址相同，hash值相同，hash值衝突;看內容是否相同

set去重原理
step1. 第一步必須求hash，hash衝突了才需要去重
step2. 第二步 去重 比較內容
'''
print({tom1, tom2}) # {Tom, Tom}

jerry = Person('Jerry')
print({tom1, tom2, jerry}) # {Jerry, Tom}

```



### 14-5-4. 容器相關的特殊方法 

#### - `__bool__`及`len__`

>  在 Python 中，`__bool__` 和 `__len__` 是用來參與「真值測試」（truth value testing）的兩個魔術方法。它們的調用時機與優先順序有明確規則，尤其在你使用 `if obj:` 或 `while obj:` 等語句時，Python 會自動決定該物件是否為「真」或「假」。

+ 調用時機與優先順序

  \- 當 Python 需要判斷一個物件的布林值時（例如 `if obj:`）：優先調用 `__bool__()`。

  \- 若物件定義了 `__bool__()`，則直接使用其回傳值（必須是 `True` 或 `False`）。

  \- 若未定義 `__bool__()`，則調用 `__len__()`。若 `__len__()` 回傳 `0`，則視為 `False`；否則視為 `True`。

  \- 若兩者皆未定義，則預設為 `True`。


| 方法       | 回傳型態 | 調用時機                     |
| ---------- | -------- | ---------------------------- |
| `__bool__` | `bool`   | 優先於 `__len__` 被調用      |
| `__len__`  | `int`    | 當 `__bool__` 未定義時被調用 |



#### - `__setitem__`: 觸發時機`obj[key]`或 `for x in obj`

#### - ` __getitem__`: 觸發時機`obj[key] = value`

#### - `__delitem`:  觸發時機`del obj[key]`或 `del obj[key1:key2]`

#### - `__contains__`: 觸發時機`value in obj`

#### - `__iter__`: 觸發時機`iter(obj)`或 `for x in obj`

>  以下方法構成了 Python 容器（sequence 或 mapping）最核心的操作協議。透過這些方法，你可以讓自訂類別像 `list`、`dict`一樣被索引、刪除、遍歷、成員測試等。

| 方法           | 觸發時機                               | 典型回傳/行為                 |
| -------------- | -------------------------------------- | ----------------------------- |
| `__getitem__`  | `obj[key]` 或 `for x in obj`           | 回傳 `obj[key]` 的值          |
| `__setitem__`  | `obj[key] = value`                     | 設定或插入 `value`            |
| `__delitem__`  | `del obj[key]` 或 `del obj[key1:key2]` | 刪除指定鍵或切片              |
| `__contains__` | `value in obj`                         | 回傳 `True` 或 `False`        |
| `__iter__`     | `iter(obj)` 或 `for x in obj`          | 回傳一個可迭代物件 (iterator) |



```python
class Cart:
    def __init__(self, **kwargs):
        if len(kwargs)==0:
            self.__items_name = []
            self.__items_index = []
            self.__items = dict()
            self.__num_of_item = 0
        else:
            self.__items = kwargs
            self.__num_of_item = len(kwargs)
            self.__items_name = list(kwargs.keys())
            self.__items_index = list(range(self.__num_of_item))


    def __setitem__(self, key, value: str|list):
        if isinstance(key, str):
            if key not in self.__items_name:
                self.__num_of_item += 1
                self.__items_index.append(self.__num_of_item - 1)
                self.__items_name.append(key)
            self.__items[key] = value

        elif isinstance(key, list):
            for i, temp in enumerate(key):
                if temp not in self.__items_name:
                    self.__num_of_item += 1
                    self.__items_index.append(self.__num_of_item - 1)
                    self.__items_name.append(temp)

                self.__items[temp] = value[i]


    def __getitem__(self, key):
        if isinstance(key, str):
            input_dict = {key: self.__items[key]}
        elif isinstance(key, list):
            input_dict = {temp: self.__items[temp] for temp in key}
        else:
            raise Exception('key error')

        # return True
        return Cart(**input_dict)


    def __iter__(self):
        yield from (self.__getitem__(key) for key in self.__items_name)


    def __repr__(self):
        # print(self.__items_name)
        # print(self.__items_index)
        return str(self.__items)

    def __contains__(self, key):
        return key in self.__items_name

    def __delitem__(self, key):
        idx = self.__items_name.index(key)
        self.__items_name.pop(idx)
        self.__num_of_item -= 1
        self.__items_index = list(range(self.__num_of_item))
        del self.__items[key]

    def __len__(self):
        return len(self.__items)


shopping_cart = Cart()

#############################################################################################
# __setitem__特殊方法實現單個及多個購物車添加
shopping_cart['購物車1'] = ['水']
shopping_cart['購物車1'] = ['好水']
shopping_cart[['購物車2', '購物車3']] = [['餅乾', '酒', '雞肉'], ['冰']]

print(shopping_cart, f'type= {type(shopping_cart)}')

###############################################################################################
# __getitem__特殊方法獲取單個及多個購物車內容
print('-'*30)
temp = shopping_cart['購物車1']
print(temp, f'type= {type(temp)}')

temp = shopping_cart[['購物車1', '購物車2']]
print(temp, f'type= {type(temp)}')

###############################################################################################
# 遍歷購物車
# it = iter(shopping_cart)
# print(next(it))
# print(next(it))
# print(next(it))
# 遍歷購物車
print('-'*30)
for cart in shopping_cart:
    print(cart, f'type= {type(cart)}')

###############################################################################################
# __contains__特殊方法 配合in關鍵字
print('-'*30)
print('購物車4' in shopping_cart)

###############################################################################################
# __delitem__特殊方法 配合del關鍵字
print('-'*30)
del shopping_cart['購物車1']
del shopping_cart['購物車3']
print(len(shopping_cart))
for cart in shopping_cart:
    print(cart, f'type= {type(cart)}')


```







## 14-6. 抽象類

### 14-6-1. 什麼是抽象類(未實現的類)

#### - 抽象類是一個`不能被實例化的類`

#### - 抽象方法是一個`沒有具體實現的方法`(子類中重寫方法)

#### - 一個抽象類可以有或沒有抽象方法

>[!NOTE]
>
>  Python沒有直接支持抽象類，但提供一個`模塊(abc)`來允許定義抽向類。

### 14-6-2. 如何定義抽象類`ABC`

#### - 通過繼承`ABC`來定義一個抽象類

```python
# 1.引入abc模塊來定義抽象類
from abc import ABC, abstractmethod


# 2.繼承ABC來定義抽象類
class Action(ABC):
    # 3. 定義抽象方法(等同c++純虛函數)(未實現方法)
    @abstractmethod
    def execute(self):
        pass

```

#### - 定義抽象方法使用`@abstractmethod`裝飾器

```python
# 2.繼承ABC來定義抽象類
class Action(ABC):
    # 3. 定義抽象方法(等同c++純虛函數)(未實現方法)
    @abstractmethod
    def execute(self):
        pass

```

### 14-6-3. 使用抽象類

>   子類繼承抽象類，重寫抽象方法。

```python
# 繼承抽象類，重寫抽象方法(純虛函數)
class CreateStudentAction(Action):
    # 如果沒有重寫抽象方法，依然是一個抽象類，則無法實例化
    def execute(self):
        print("CreateStudentAction執行了")

```

### 14-6-4. 抽象屬性

>  在 Python 中，抽象屬性是指在抽象基底類別（Abstract Base Class，ABC）中宣告的屬性，需要由所有子類別實作其 getter 與 setter，否則在實例化時會拋出 `TypeError`，確保各子類別提供一致的屬性介面

```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @property
    @abstractmethod
    def abstract_property(self):
        """子類別必須實作此 getter"""
        pass

    @abstract_property.setter
    @abstractmethod
    def abstract_property(self, value):
        """子類別必須實作此 setter"""
        pass
```

>[!NOTE]
>
>1. `AbstractClass`繼承自`ABC`，代表它是一個抽象基底類別。
>2. 先用`@abstractmethod`標記它是抽象方法，再用 `@property` 設定getter。
>3. 接著用`@abstractmethod`與`@abstract_property.setter`標記setter。
>4. 子類別若未同時實作 getter 與 setter，就無法被實例化。



範例: 14_類



---





# 教學資源

https://www.youtube.com/watch?v=K2EZ-beTdGM&list=PLmOn9nNkQxJFGvtKd7PI7AhsYmY-6FrJs&index=100