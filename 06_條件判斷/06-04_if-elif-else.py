"""
    if-elif-else語句
    語法:
        if 條件表達式:
            代碼塊
        elif 條件表達式:
            代碼塊
            .
            .
            .
        else:
            代碼塊

    執行流程:
        if-elif-else在執行時，會自上向下依次對條件表達式進行求值判斷
            如果表達式結果為True，則執行當前代碼塊，然後語句結束
            如果表達式結果為False，則繼續向下判斷，直到找到True為止
            如果所有表達式都為False，則執行else後的代碼塊
"""

age = 70

if age > 200:
    print('活著可真沒勁呢!')
elif age > 100:
    print('你也老大不小了!')
elif age >= 60:
    print('你已經退休了!')
elif age >= 30:
    print('你已經中年了!')
elif age >= 18:
    print('你已經成年!')
else:
    print('你還是個小孩!')


