# 開箱即用
# 為了實現開箱即用的功能，Python中為我們提供了一個模塊的標準庫
# 這個標準庫中，有很多強大的模塊我們可以直接使用
#   並且標準庫會隨Python的安裝一同安裝

# sys模塊，它裡面提供了一些變量和函數，使我們可以獲取到Python解析器的訊息
#  或者通過函數來操作Python解析器
# 引入sys模塊
import sys
import pprint

sys.argv
# 獲取執行代碼時，命令行中所包含的參數
# 該屬性是一個列表，列表中保存了當前命令的所有參數
print(sys.argv)

# sys.modules
# 獲取當前程序中引入的所有模塊
# modules是一個字典，key是模塊名，value是模塊對象
pprint.pprint(sys.modules)

# pprint模塊它給我們提供了一個方法pprint() 該方法可以用來對打印的數據做簡單格式化處理

# sys.path
# 它是一個列表，列表中保存的是模塊的搜索路徑
pprint.pprint(sys.path)

# sys.platform
# 表示當前Python運行的平台
print(sys.platform)

# sys.exit()
# 函數用來退出程序
# sys.exit()

# os 模塊讓我們可以對操作系統行訪問
import os

# os.environ
# 通過這個屬性可以獲取到系統的環境變量
print(os.environ['path'])

# os.system()
# 可以用來執行操作系統的命令
os.system()