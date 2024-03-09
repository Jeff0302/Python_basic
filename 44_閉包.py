# 將函數作為返回值返回，也是一種高階函數
# 這種高階函數我們也稱為閉包，通過閉包可以創建一些只有當前函數能訪問的變量
#   可以將一些私有的數據藏到閉包中

def fn():
    a = 10
    # 函數內部再定義一個函數
    def inner():
        print('我是fn2', a)
    # 將內部函數inner作為返回值返回
    return inner

# r是一個函數，是調用fn()返回的函數
# 這個函數是在fn()內部定義的，並不是全局函數
# 所以這個函數總是能訪問到fn()函數內部的變量
r = fn()
r()

# 求多個數的平均值
# nums = [50, 30, 20, 10, 77]

# sum()用來求列表中所有元素的和
# print(sum(nums)/len(nums))

# 創建一個列表，用來保存數值

# 形成閉包的要件
# 1. 函數嵌套
# 2. 將內部函數作為返回值返回
# 3. 內部函數必須使用到外部函數的變量
def make_average():
    nums = []

    # 創建一個函數，用來算平均值
    def average(n):
        # 將n添加到列表中
        nums.append(n)
        # 求平均值
        return sum(nums)/len(nums)

    return average


average = make_average()
print(average(10))
print(average(10))
print(average(30))