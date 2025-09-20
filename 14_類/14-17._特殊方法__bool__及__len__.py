class Cart:
    pass
    # def __bool__(self):
    #     print('__bool_被調用了')
    #     return True

    # def __len__(self):
    #     print('__len__被調用了')
    #     return 0


shopping_cart = Cart()
print(bool(shopping_cart))
'''
當對對象取bool()時，會先看__bool__是不是有被定義，如果定義了就使用。
沒有定義建會看__len__是不是有定義，有定義只要len返回>0就返回True，反之則返回False
'''

# if shopping_cart:
#     pass
