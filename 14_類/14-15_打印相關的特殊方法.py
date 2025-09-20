import json


class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def __str__(self):
        return f'[__str__] name= {self.name}, age= {self.age}'

    def __repr__(self):
        return f'[__repr__] name= {self.name}, age= {self.age}'

    def __bytes__(self):
        return json.dumps(self.__dict__).encode()

p1 = Person('Jeff', age=20)

print(p1)
print(str(p1))
print(f'{p1}')

print([p1, p1]) # []使用__str__，但其內部使用__repr__
print([str(p1)]) # []使用__str__，其中元素使用str()也使用__str__

print(bytes(p1))

'''
[__str__] name= Jeff, age= 20
[__str__] name= Jeff, age= 20
[__str__] name= Jeff, age= 20
[[__repr__] name= Jeff, age= 20, [__repr__] name= Jeff, age= 20]
['[__str__] name= Jeff, age= 20']
b'{"name": "Jeff", "age": 20}'

'''