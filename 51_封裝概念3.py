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
