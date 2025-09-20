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


print('-'*50)


# 練習: 設計2維座標類Point，使其成為可hash類型，並比較兩座標是否相等
from collections.abc import Hashable


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))


    def __eq__(self, other):
        return (self.x == other.x) & (self.y == other.y)


p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)

print(isinstance(p1, Hashable))