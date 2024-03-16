class A(object):

    # 類屬性
    # 實例屬性
    # 類方法
    # 實例方法
    # 靜態方法

    # 類屬性，直接在類中定義的屬性是類屬性
    # 類屬性可以通過類和類的實例訪問到
    # 但是類屬性只能通過類對象來修改，無法通過實例對象來修改
    count = 0

    def __init__(self):
        # 實例屬性，通過實例對象添加的屬性屬於實例屬性
        # 實例屬性只能通過實例對象訪問和修改，類對象無法訪問修改
        self.name = '孫悟空'

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
        print('這是test2方法~~', cls)

    # 靜態方法
    # 在類中使用 @staticmethod 來修飾的方法屬於靜態方法
    # 靜態方法不需要指定任何默認參數，靜態方法可以通過類和實例調用
    # 靜態方法基本上是一個和當前類無關的方法，它只是保存到當前類中的函數
    # 靜態方法一般都是一些工具方法，和當前類無關
    @staticmethod
    def test3():
        print('這是test3方法')

a = A()
# 實例屬性，通過實例對象添加的屬性屬於實例屬性
# a.count = 1
A.count = 100
print(a.count, ' ', id(a.count))
print(A.count, ' ', id(A.count))

print(a)
# a.test()等價於A.test(a)
a.test()
A.test(a)

print(A)
A.test2()
a.test2()

A.test3()
a.test3()