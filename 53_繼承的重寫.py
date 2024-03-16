class Animal:
    def run(self):
        print('動物會跑')

    def sleep(self):
        print('動物睡覺')

class Dog(Animal):
    def bark(self):
        print('狗在嚎叫~~')

    def run(self):
        print('狗跑~~')


# 如果在子類中有和父類同名的方法，則通過子類實例化的對象去調用方法時，會調用子類的方法，而不是父類
#  這個特點我們稱為方法的重寫(覆蓋, override)
# 創建一個Dog類的實例
d = Dog()
d.run()

# 當調用一個對象的方法時
#  會優先去當前對象中尋找是否具有該方法，如果有則直接使用
#  如果沒有會去當前對象的父類中尋找，如果父類中有該方法，則直接調用父類中的方法
#  如果沒有，則去父類的父類中尋找，以此類推，直到找到object為止，如果依然沒找到則報錯
