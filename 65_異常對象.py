

print('異常出現前')

try:
    1 + 'hello'
    print(10/0)
    print(c)
except NameError:
    # 如果except後不跟任何內容，則此時它會捕獲到所有的異常
    # 如果在except後跟著一個異常類型，那麼此時它只會捕獲該類型的異常
    print('出現NameError異常')
except ZeroDivisionError:
    print('出現ZeroDivisionError異常')
# Exception是所有異常類的父類，所以如果except後跟的是Exception，它也會捕獲所有異常
# 可以在異常類後邊跟著一個as xx，此時xx就是異常對象
except Exception as e:
    print('未知異常', e, type(e))
finally:
    print('無論是否出現異常，該子句都會執行')


print('異常出現後')