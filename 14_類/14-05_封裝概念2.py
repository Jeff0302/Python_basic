# 可以為對象的屬性使用雙下划線開頭, __xxx
# 雙下划線開頭的屬性，是對象的隱藏屬性，隱藏屬性只能在類中訪問，無法通過對象訪問
# 其實隱藏屬性只不過是Python自動為屬性改了一個名字
#   實際是將屬性名修改為  _類名__屬性名

# 使用__開頭的屬性，實際上依然可以在外部訪問，所以這種方式我們一般不用
#   一般我們會將一些私有屬性(不希望被外部訪問的屬性)以_開頭
#   一般情況下，使用_開頭的屬性都是私有屬性，沒有特殊需要時，不要修改私有屬性

# 函數的保護與私有與上述規則一致

class Person:
    def __init__(self, name, age):
        self.name = name
        self._money = 0
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


