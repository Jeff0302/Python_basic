# 讓用戶在控制台中輸入一個年齡
age = input('請輸入你的年齡:')

# 如果用戶大於18歲，則顯示你已經成年
if int(age) >= 18:
    print('你已經成年!')
else:
    print('你還未成年!')
"""
    if-else語句
    語法:
        if 條件表達式:
            代碼塊
        else:
            代碼塊
            
    執行流程: 
        if-else在執行時，先對if後的條件表達式進行求值判斷
            如果為True，則執行if後的代碼塊
            如果為False，則執行else後的代碼塊
            
        
"""
