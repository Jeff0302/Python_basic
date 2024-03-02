# 遍歷字典
# keys()    該方法會返回字典的所有key
# 該方法會返回一個序列，序列中保存所有字典的key
d = {'name': '孫悟空', 'age': 18, 'gender': '男'}

# 通過遍歷keys()來獲取所有鍵
for key in d.keys():
    print(key, d[key])

print(d.keys())
# values()  該方法會返回字典的所有value
print(d.values())
for value in d.values():
    print(value)

# items()
# 該方法會返回字典中的所有項
# 它會返回一個序列，序列中包含雙值子序列  [(k1,v1),(k2,v2),....]
# 雙值分別是，字典中的key和value
for k, v in d.items():
    print(k, v)