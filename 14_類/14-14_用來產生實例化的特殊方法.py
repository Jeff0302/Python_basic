class Person:
    def __new__(cls, *args, **kwargs):
        print('cls= ',cls)
        print('args= ', args)
        print('kwargs ', kwargs)
        print('__new__被調用了')
        # __new__必須返回一個實例，反__init__不會被調用
        # 如何創建實例
        # 1. 不可以自己創建，會造成遞規創建
        # 2. 通過父類的實例方法__new__來創建並返回實例，__new__是一個靜態方法必需手動傳參
        return super().__new__(cls)
        # 錯誤: RecursionError: maximum recursion depth exceeded while calling a Python object
        # return cls(*args, **kwargs)

    def __init__(self, name, age=18):
        # 在 __new__ 返回後被調用
        print('__init__被調用了')
        self.name = name
        self.age = age


p1 = Person('Jeff', age=20)
print(p1)

'''
cls=  <class '__main__.Person'>
args=  ('Jeff',)
kwargs  {'age': 20}
__new__被調用了
__init__被調用了
<__main__.Person object at 0x000001546D09E050>
'''