# 邏輯運算符
"""
    邏輯運算符主要用來做一些邏輯判斷
    not 邏輯非
        not可以對符號右邊值進行非運算
           對於布爾值，非運算會對其進行取反操作,True變False,False變True
           對於非布爾值，非運算會先將其轉換為布爾值,然後再取反
    and 邏輯與
        and可以將符號兩側的值進行與運算
           只有在符號兩側值都回True時,才會返回True,只要有一個False則返回False
           與運算是找False
           Python中的與運算是短路的與，如果第一個值是False,則不看第二個

    or  邏輯或
        or可以對符號兩側的值進行或運算
          或運算兩個值中只要有一個為True,就會返回True
          或運算是找True
          Python中的或運算是短路的或，如果第一個值是True,則不看第二個

"""

a = True
a = not a   # 對a取反
a = 1
a = not a   # False
print('a= ', a)

result = True and True      # True
result = True and False     # False
result = False and True     # False
result = False and False    # False

False and print('你猜我出來出來嗎?')
True and print('你猜我出來出來嗎?')

result = True or True      # True
result = True or False     # True
result = False or True     # True
result = False or False    # False

print(result)

True or print('你猜我出來出來嗎?')

# 非布爾值的與或運算
# 當我們對非布爾值進行與或運算時，Python會將其當作布爾值運算，最終返回原值
# 與運算規則
#   與運算是找false的，如果第一個是false，則不看第二個
#   如果第一個值是false則直接返回第一個，否則返回第二個值
# 或運算規則
#   或運算是找true的，如果第一個是true，則直接返回第一個
#   如果第一個值是false，則返回第二個值
result = 1 and 2    # 2
result = 1 and 0    # 0
result = 0 and 1    # 0
result = 0 and None    # 0

result = 1 or 2  # 1
result = 1 or 0  # 1
result = 0 or 1  # 1

result = 0 or None  # None


print("result=", result)







