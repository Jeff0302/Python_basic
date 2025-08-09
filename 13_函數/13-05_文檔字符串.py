# help()是Python中的內置函數
# 通過語法help()函數可以查詢Python中的函數用法
# 語法: help(函數對象)


print(help(print))

# 文檔字符串(doc str)
# 在定義函數時，可以在函數內部編寫文檔字符串，文檔字符串就是函數的說明
#   當我們編寫了文檔字符串，我們就可以通過help()函數來查看函數的說明
# 文檔字符串非常簡單，就是在函數的第一行寫下的字符串就是文檔字符串


def fn(a: int, b: bool, c: str = 'hello') -> int:
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    return 10

help(fn)