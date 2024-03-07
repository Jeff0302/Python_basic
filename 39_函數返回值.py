# 返回值
# 返回值就是函數執行以後返回的結果
# 可以通過return來指定函數的返回值
# return之後可以跟任意數據類型，返回值甚至可以是一個函數
# 如果只寫一個return或不寫return，則相當於return None
# 在函數中，return後的代碼都不會執行， return一執行函數自動結束

def sum(*nums):
    # 定義一個變量保存結果
    result = 0
    # 遍歷元組，並將元組中的元素進行累加
    for num in nums:
        result += num
    return result

print(sum(123, 456, 789))


def fn():
    return 10

# fn和fn()的區別
print(fn)       # fn是函數對象，打印fn實際是在打印函數對象    <function fn at 0x0000013C1A2E8860>
print(fn())     # fn()是在調用函數，打印fn()實際是在打印fn()函數的返回值