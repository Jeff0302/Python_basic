# 創建幾個函數
import random

def add(a, b):
    """
        求任意兩數和
    """
    r = a + b
    return r


def mul(a, b):
    """
          求任意兩數積
      """
    r = a * b
    return r

# 希望函數可以在計算前，打印開始計算，計算結束後打印計算完畢
#  我們可以直接通過修改函數中的代碼來完成這個需求，但是會產生以下一些問題
#  1. 如果要修改的函數過多，修改起來會比較麻煩
#  2. 並且不方便後期維護
#  3. 並且這樣會違反開閉原則(OCP)
#        程序的設計，要求開放對程序的擴展，關閉對程序的修改
# 在定義函數時，可通過@裝飾器，來指定使用的裝飾器，來裝飾當前的函數
# 可以同時為一個函數指定多個裝飾器，這樣函數將會依照由內向外的順序被裝飾

# 我們希望在不修改原函數的情況下，來對函數進行擴展
def fn():
    print('我是fn函數....')

# 只需要根據現有的函數，來創建一個新的函數
def fn2():
    print('函數開始執行~~~')
    fn()
    print('函數執行結束~~~')

fn2()

# 上述方式已經可以在不修改原代碼的情況下對函數進行擴展
#   但是，這種方式要求我們每擴展一個函數就要手動創建一個新的函數，實在是太麻煩了
# 為了解決一個問題，我們創建一個函數，讓這個函數可以自動幫我們生產函數

def begin_end(old):
    """
        用來對其他函數進行擴展，使其他函數可以在執行前打印函數開始執行，在函數結束後打印函數執行結束
        參數:
            old 要擴展的函數對象
    """
    # 創建一新的函數
    def new_function(*args, **kwargs):
        print('函數開始執行~~~')
        # 調用被擴展的函數
        r = old(*args, **kwargs)
        print('函數執行結束~~~')
        return r

    # 返回新函數
    return new_function

def fn3(old):
    """
        用來對其他函數進行擴展，使其他函數可以在執行前打印函數開始執行，在函數結束後打印函數執行結束
        參數:
            old 要擴展的函數對象
    """
    # 創建一新的函數
    def new_function(*args, **kwargs):
        print('fn3裝飾器~~~')
        # 調用被擴展的函數
        r = old(*args, **kwargs)
        print('fn3裝飾器~~~')
        return r

    # 返回新函數
    return new_function

f = begin_end(mul)
# f2 = begin_end()
# print(f)
# print(f2)
print(f(5, 3))

# 向begin_end()這種函數我們就稱之為裝飾器
#  通過裝飾器，可以在不修改原函數的情況下，對函數進行擴展
#  在開發中，我們都是通過裝飾器來擴展函數功能
@begin_end
@fn3
def say_hello():
    print('大家好~~~')

say_hello()

# 應用情境
#########################################################################
'''
假設我們已經定義了一個函數task，這個函數接受一個變量並返回一個執行結果
ex: 自動測試中給定的測試參數，返回一個測試結果

利用裝飾器來達到多次執行的多功能，但我們又希望每次執行的輸入參數是變動的
*使用帶參數的裝飾器

ex:
run1 param1-1,param1-2
run2 param2-1,param2-2
run3 param3-1,param3-2
run4 param4-1,param4-2
run5 param5-1,param5-2

'''
def multi_run_script(runs: list):
    def multi_run(task):
        def multi_run_task(*args, **kwargs):
            result = []
            for i in range(len(runs)):
                # 將多次執行結果返回到一個列表之中
                result.append(task(*runs[i]))

            return result

        return multi_run_task

    return multi_run


from functools import wraps

def multi_run_5times(task):
    @wraps(task)
    def multi_run_task(*args, **kwargs):
        result = []
        for i in range(5):
            # 將多次執行結果返回到一個列表之中
            result.append(task(*args))

        return result

    return multi_run_task


@multi_run_5times
# @multi_run_script([('1-1', '1-2'), ('2-1', '2-2'), ('3-1', '3-2')])
def task(*test_params):

    test_results =  *test_params, random.randint(0, 100), random.randint(10, 20)
    # print(test_results)
    return test_results

# 執行1次task的結果
print(task.__wrapped__('1-1', '1-2'))
# ('1-1', '1-2', 65, 14)
# 執行五次task的結果
print(task('1-1', '1-2'))

# 執行多次task的結果
# 動態調用方式
runs = ((str(i)+'-1', str(i)+'-2')for i in range(1, 4))
print(multi_run_script(list(runs))(task.__wrapped__)())
# [('1-1', '1-2', 31, 17), ('2-1', '2-2', 90, 14), ('3-1', '3-2', 81, 17)]

#########################################################################
