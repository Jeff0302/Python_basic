# 就像我們生活中會產生垃圾一樣，程序在運行過程當中也會產生垃圾
# 程序運行當中的垃圾會影響到程序運行的效能，所以這些垃圾必須被即時清理
# 沒有用的東西就是垃圾
# 在程序中沒有被引用的對象就是垃圾，這種圾垃對象過多以後會影響到程序的運行效能
#  所以我們必須進行即時的垃圾回收，所謂的垃圾回收就是將垃圾對象從內存中刪除
# 在Python中有自動的圾垃回收機制，它將會自動將沒有被引用的對象刪除
#  所以我們不用手動處理垃圾回收

class A:
    def __init__(self):
        self.name = 'A類'

    # del是一個特殊方法，它會在對象被垃圾回收前調用
    def __del__(self):
        print('A()對象被刪除了~~~~', self)


a = A()

# b = a

# 將a設置為了None，此時沒有任何變量對A()對象進行引用，它就變成了垃圾
a = None

input('回車鍵退出...')