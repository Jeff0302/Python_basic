# match-case的使用
"""
語法

    match 變量名:
        case 變量值1:
            代碼塊
        case 變量值2:
            代碼塊
        .
        .
        .
        case _:
            代碼塊


    執行流程:
        判斷變量是否與變量值1相同，如果相同則執行變量值1下的代碼塊。
        如果不相同判斷變量是否與變量值2相同，如果相同則執行變量值2下的代碼塊。
        如果不相同判斷變量是否與變量值3相同，如果相同則執行變量值3下的代碼塊。
        如果變量沒有找到相同的case，則執行case _下方的代碼塊。


"""
name = 'CJ'


match name[0]:
    case 'A':
        print('name[0] = A')
    case 'B':
        print('name[0] = B')
    case 'C':
        print('name[0] = C')
    case _:
        print(f'default case name[0] = {name[0]}')






