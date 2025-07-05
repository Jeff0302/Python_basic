from enum import Enum
"""
    字典(dict)
    - 字典屬於一種新的數據結構，稱之為映射(mapping)
    - 字典的作用和列表類似，都是用來儲存對象的容器
    - 列表存儲數據的性能很好，但查詢數據的性能很差
    - 在字典中每一個元素都有唯一的名字，通過這個唯一的名子可以快速地查找到指定的元素
    - 在查詢元素時，字典的效率是非常快的
    - 字典中也是可以保存多個對象，每個對象都會有一個唯一的名子
      這個唯一的名子,我們稱之為key(鍵)，通過key可以快速查找value
      這個對象，我們稱其為value(值)
      所以字典，我們也稱為鍵值對結構(key-value)
      每個字典中都可以有多個鍵值對，而每一個鍵值對，我們稱值為item
"""

# 創建一個空字典
# 使用{}來創建字典
my_dict = {}
# my_dict = dict()
print(type(my_dict))

# 創建一個有數據的字典
# 語法:
#       {key: value, key: value, key: value..}
#   字典的值可以是任意對象
#   字典的key可以是任意的不可變對象(int、str、bool、tuple...)，但一般我們都會使用str
#   字典的key是不能重複的，如果出現重複的，後面會替換到前邊的
d = {'name': '孫悟空', 'age': 18, 'gender': '男'}
print(d)

# 可以根據鍵來獲取值
print(d['name'], d['age'], d['gender'])
# 如果使用字典中不存在的鍵值，會抱錯
# print(d['hello'])  KeyError: 'hello'


class Student():
    class Infos:
        name = 'name'
        age = 'age'
        gender = 'gender'

    def __init__(self, name: str, age: int, gender: str):
        self.info = {'name': name, 'age': age, 'gender': gender}

jeff = Student('Jeff', 18, '男')
print(jeff.info[Student.Infos.name])

