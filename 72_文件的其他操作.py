import os
from pprint import pprint

# os.listdir() 獲取指定路徑的目錄結構
# 需要一個路徑作為參數，會獲取到該路徑下的目錄結構，默認路徑為.當前目錄
# 該方法會返回一個列表，目錄中的每個文件(夾)名字都是列表中的一個元素
r = os.listdir()
pprint(r)

# os.getcwd() 獲取當前所在的目錄
print(os.getcwd())

# os.chdir() 切換當前所在目錄
os.chdir('..')
print(os.getcwd())

# 創建目錄
# 在當前路徑下創建一個名子為aaa的目錄
# os.mkdir('aaa')

# 刪除目錄
# os.rmdir('aaa')

# open('aa.txt', mode='w')
# 刪除文件
# os.remove('aa.txt')

# 重新命名文件
# 可以對一個文件進行重新命名，也可以用來移動一個文件
# os.rename('舊名子', '新名子')
# os.rename('舊名子', 'C:/Users/Public/Desktop/舊名子')

