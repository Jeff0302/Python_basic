# 函數式編程
#   -在Python中，函數是一等對象
#   -一等對象一般都有如下特點:
#       1. 對象是在運行時創建的
#       2. 能賦值給變量或是作為數據結構中的元素
#       3. 能作為參數傳遞
#       4. 能作為返回值返回
#   -高階函數
#       高階函數至少要符合以下兩個特點中的一個
#       1. 接收一個或多個函數作為參數
#       2. 將函數作為返回值返回


# 創建一個列表
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 定義一個函數
#   可以將只指定列表中的所有偶數，保存到一個新列表中返回
# 當我們使用一個函數作為參數時，實際上就是將指定的代碼傳進了目標函數

def is_even(n: int):
    return not bool(n % 2)


def fn(input_list: list, fun):
    """
        fn()函數可以將指定列表中的所有偶數獲取出來，並保存到一個新的列表中返回

        參數 input_list: 要進行篩選的列表
            fun: 要篩選的條件
    """
    # 創建一個新列表
    result = []
    # 對列表進行篩選
    for element in input_list:
        # 判斷element的奇偶
        if fun(element):
            result.append(element)
    # 返回新列表
    return result


print(fn(l, is_even))

