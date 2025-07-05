# 創建字典
# 使用{}
# 語法: {key: value, key: value, key: value}

# 使用dict()函數來創建字典
# 每一個參數都是一個鍵值對，參數名就是鍵，參數值就是值(這種方式創建的字典，key都是字符串)
d = dict(name='孫悟空', age=18, gender='男')
print(d, type(d))

# 也可以將一個雙值子序列的序列轉換為字典
# 雙值序列 [1, 2] ('a', 3) 'ab'
# 子序列: 如果序列中元素也是序列，那我們就稱這個元素為子序列
# [(1, 2), (3, 4)]
d = dict([('name', '孫悟空'), ('age', 18), ('gender', '男')])
print(d, type(d))

# len()函數 獲取字典內鍵值對的個數
print(len(d))

# in 檢查字典內是否有包含指定的鍵
# not in 檢查字典內是否沒有包含指定的鍵
print('name' in d)
print('aaa' not in d)

# 獲取字典中的值
# 語法: d[key]
print(d['name'])

# n = 'name'
# d[n]
# 通過[]來獲取值時，如果鍵不存在，會拋出異常KeyError

# get(key[, default]) 該方法用來根據鍵獲取字典的值
# 如果獲取的鍵在不在字典中，則返回none
# 也可以指定一個默認值，來作為第二個參數，這樣獲取不到值時，會返回默認值
print(d.get('aaa', '默認值'))

# 修改/新增字典
# d[key] = value  如果key存在則覆蓋，不存在則添加
d['name'] = 'Jeff'
print(d)
d['address'] = '花果山'
print(d)

# setdefault(key[, default])
# 可以用來向字典中添加鍵字對
# 如果鍵值存在則不會覆蓋，鍵值不存在就會添加key-value
d.setdefault('電話', '1111')
print(d)

# update([other])
# 將其他字典中的key-value，添加到當前字典中
# 如果有重複的key，後面的會替換當前的
d = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 6, 'f': 6, 'a': '7'}
d.update(d2)
print(d)

# 刪除，可以使用del[key]來刪除字典中的key-value
# 如果刪除不存在的key，它會拋出異常
del d['a']
del d['b']
print(d)
# popitem()
# 隨機刪除字典中的鍵值對，一般會刪除最後一個鍵值對
#   刪除之後，它會將刪除的key-value做為返回值返回
#   返回的是一個元組，元組中有兩個元素，第一個是刪除的key，第二個是刪除的value
# 當使用popitem刪除一個空字典時，會拋出異常KeyError: 'popitem(): dictionary is empty'
result = d.popitem()
print(result)

# pop(key[, default])
# 根據key刪除字典中的key-value
# 會將被刪除的value返回
# 如果刪除不存在的key，它會拋出異常
#   如果指定了默認值，再刪除不存在的key，不會報錯，而是直接返回默認值
result = d.pop('e')
result = d.pop('z', '默認值')

# clear() 用來清空字典
d.clear()

print('result=', d)

# copy()
# 該法方用來對字典進行淺複製
# 複製以後的對象和原對象是獨立，修改一個不會影響另一個
#  注意，淺複製只會簡單複製對象內的值，如果值也是一個可變對象，這個可變對象不會被複製
d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d
d2 = d.copy()
print('d=', id(d))
print('d2=', id(d2))

d = {'a': {'name': 'Jeff', 'age': 18, 'gender': '男'}, 'b': 2, 'c': 3}
d2 = d.copy()
d2['a']['name'] = '豬八戒'
print(d)
print(d2)

print("d['a']", id(d['a']))
print("d2['a']", id(d2['a']))






