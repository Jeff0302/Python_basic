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

# filter()
# filter()可以從序列中過濾出符合條件的元素，保存到一個新的序列中
# 參數:
#   1. 函數，根據該函數來過濾序列(可疊代結構)
#   2. 需要過濾的序列(可疊代結構)
# 返回值:
#    過濾後的新序列(可疊代結構)

# is_even是最作為參數傳遞進filter()函數中的
#   而is_even實際上只有一個作用，就是作為filter()的參數
#   filter()調用完畢以後，is_even就已經沒用
print(list(filter(is_even, l)))

# 匿名函數lambda函數表達式(語法糖)
#  lambda函數表達式專門用來創建一些簡單的函數，它是函數創建的另一種方式
# 語法:
#      lambda 參數列表: 返回值
# 匿名函數一般都是作為參數使用，其他地方不會使用

# 可以將一個匿名函數賦值給一個變量，一般不會這麼做
fn2 = lambda x, y: x + y
print(fn2(1, 3))

print(list(filter(lambda x: x % 2 == 0, l)))

# map()
# map()函數可以對可疊代對象中的所有元素進行指定操作，並將結果添加到一個新的可疊代對象中返回
print(list(map(lambda x: x + 1, l)))

# sort()
# 該方法用來對列表中的元素進行排序
# sort()方法默認是直接比較列表中元素的大小
# 在sort()可以接受一個關鍵字參數 key
#   key需要一個函數作為參數，當設置了函數作為參數
#   每次都會以列表中的一個元素作為參數來調用函數，並使用函數的返回值大小來進行排序
l = ['bb', 'aaaa', 'c', 'ddddddd', 'fff']
l.sort(key=len)
print(l)

l = [2, 5, '1', 3, '6', '4']
l.sort(key=int)
print(l)

# sorted()
# 這個函數和sort()用來基本一致，但是sorted()可以對任意序列進行排序
#   並且使用sorted()排序不會影響原來的對象，而是返回一個新的對象
l = [2, 5, '1', 3, '6', '4']
print('排序前l:', l)
ln = sorted(l, key=int)
print('排序後l:', l)
print('ln:', ln)
