# 拋出異常
#   - 可以用raise語句來拋出異常
#      raise語句後需要跟一個異常類 或 異常對象(實例)

# 也可以自訂義異常類，只需要創建一個類繼承Exception
class NegativeValue(Exception):
    pass


def add(a, b):
    # 如果a和b中有負數，就向調用處拋出異常
    if a < 0 or b < 0:
        # raise用於向外部拋出異常，後面可以跟一個異常類或異常類的實例
        # 拋出異常的目的，告訴調用者這裡調用時出現問題，希望你自己處理一下
        # 也可以通過if else來代替異常的處理
        # raise Exception('兩個參數中不能有負數')
        raise NegativeValue('自訂義的異常')
        # return none
    else:
        return a + b

print(add(-123, 456))
