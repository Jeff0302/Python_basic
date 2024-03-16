# 封裝是面向對象的三大特性之一
# 封裝指的是隱藏對象中不希望被外部訪問的屬性或方法
# 如何隱藏一個對象中的屬性?
#   - 將對象的屬性名，修改為一個外部不知道的名字
# 如何獲取(修改)對象中的屬性?
#   - 需要提供一個getter和setter方法，使外部可以訪問到該屬性
#   - getter獲取對象中的屬性名(get_屬性名)
#   - setter用來設置對象的指定屬性(set_屬性名)
# 使用封裝的確增加了類定義的複雜程度，但也確保了數據的安全性
#  1. 隱藏了屬性名，使調用者無法隨意更改對象中的屬性
#  2. 增加了getter和setter方法，可以很好的控制屬性是否是只讀的
#     如果希望屬性是只讀的，則可以直接去掉setter
#     如果不希望屬性被外部訪問，則可以直接去掉getter
#  3. 使用setter方法設置屬性，可以增加數據的校驗，確保數據值是否是正確的
#  4. 使用getter方法獲取屬性，使用setter方法設置屬性
#     可以在讀取屬性和設置屬性的同時進行其他的處理

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


