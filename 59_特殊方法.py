# 特殊方法，也稱作魔術方法
# 特殊方法都是使用__開頭和結尾
# 特殊方法一般不用我們自己手動調用，需要在一些特殊情況自動執行

# 定義一個Person類
class Person:
    """人類"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__()這個個特殊方法會在嘗試將對象換為字符串時調用
    # 它的作用可以用來指定對象轉換為字符串的結果
    def __str__(self):
        return 'Person [name=%s, age=%d]' % (self.name, self.age)

    # __repr__()這個特殊方法會在對當前對象使用repr()這個函數時調用
    # 它的作用是指定對象在 "交互模式" 中直接輸出的效果
    def __repr__(self):
        return 'Hello'

    # __gt__會在對象做大於比較的時後調用，該方法的返回值將會作為比較的結果
    # 它需要兩個參數，一個self表示當前對象，一個other表示和當前對象比較的對象
    # self > other
    def __gt__(self, other):
        return self.age > other.age

    # 可以通過bool()來指定對象轉換布爾值的情況
    def __bool__(self):
        return self.age > 18

# __lt__ 小於
# __le__ 小於等於
# __eq__ 等於
# __ne__ 不等於
# __gt__ 大於
# __ge__ 大於等於
# __len__()獲取對象的長度
# __bool__()

# 創建兩個Person類的實例
# 當我們打印一個對象時，實際上是打印對象中的特殊方法__str__()的返回值
p1 = Person('孫悟空', 8)
p2 = Person('豬八戒', 28)

# 打印p1 # <__main__.Person object at 0x00000221D668F950>
print(p1)
#print(repr(p1))
print(p1 > p2)
# print(bool(p1))
if p1:
    print(p1.name, '已經成年')
else:
    print(p1.name, '未成年')