# 模塊(Module)
# 模塊化，模塊化是指將一個完整的程序分解為一個一個小的模塊
#   通過將模塊組合，來搭建一個完整的程序
# 不採用模塊化，統一將所有的代碼編寫到一個文件中
# 採用模塊化，將程序編寫到多個文件
#  模塊化優點:
#    1. 方便開發
#    2. 方便維護
#    3. 模塊可以復用

# 在Python中一個py文件就是一個模塊，要想創建模塊，實際上就是創建一個Python文件
# 注意: 模塊名要符合標誌符規範

# 在一個模塊中引入外部模塊
# 1. import 模塊名(模塊名，就是Python文件名，注意不要.py)
# 2. import 模塊名 as 模塊別名
#   - 可以引入同一個模塊多次，但是模塊的實例只會創建一個
#   - import可以在程序任意位置調用，但一般情況下，import語句都會統一寫在程序的開頭
#   - 在每一個模塊內部都有一個__name__屬性，通過這個屬性可以獲取到模塊名子
#   _ __name__屬性值為__main__的模塊是主模塊，一個程序中只會有一主模塊
#      主模塊就是我們直接通過Python執行的模塊
# import module.test_module as test_module
# print(test_module.__name__)
# print(__name__)

# import module.m as m
# 訪問模塊中的變量: 模塊名.變量名
"""
print(m.a, m.b)

m.test()
m.test2()

p1 = m.Person('孫悟空')
"""

def test2():
    print('這是主模塊的test2')

"""
# 也可以只引入模塊中的部分內容
# 語法: from 模塊名 import 變量, 變量
from module.m import a, b, test, Person

# 也可以為引入的變量使用別名
# 語法:  from 模塊名 import 變量 as 別名
from module.m import test2 as new_test2
# from module.m import *  # 引入模塊中所有內容，一般不會使用
print(a)
print(b)
test()
new_test2()
p1 = Person('孫悟空')
"""
from module.m import _c
print(_c)





