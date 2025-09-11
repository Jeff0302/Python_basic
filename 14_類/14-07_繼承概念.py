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
