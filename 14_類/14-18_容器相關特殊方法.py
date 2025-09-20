class Cart:
    def __init__(self, **kwargs):
        if len(kwargs)==0:
            self.__items_name = []
            self.__items_index = []
            self.__items = dict()
            self.__num_of_item = 0
        else:
            self.__items = kwargs
            self.__num_of_item = len(kwargs)
            self.__items_name = list(kwargs.keys())
            self.__items_index = list(range(self.__num_of_item))


    def __setitem__(self, key, value: str|list):
        if isinstance(key, str):
            if key not in self.__items_name:
                self.__num_of_item += 1
                self.__items_index.append(self.__num_of_item - 1)
                self.__items_name.append(key)
            self.__items[key] = value

        elif isinstance(key, list):
            for i, temp in enumerate(key):
                if temp not in self.__items_name:
                    self.__num_of_item += 1
                    self.__items_index.append(self.__num_of_item - 1)
                    self.__items_name.append(temp)

                self.__items[temp] = value[i]


    def __getitem__(self, key):
        if isinstance(key, str):
            input_dict = {key: self.__items[key]}
        elif isinstance(key, list):
            input_dict = {temp: self.__items[temp] for temp in key}
        else:
            raise Exception('key error')

        # return True
        return Cart(**input_dict)


    def __iter__(self):
        yield from (self.__getitem__(key) for key in self.__items_name)


    def __repr__(self):
        # print(self.__items_name)
        # print(self.__items_index)
        return str(self.__items)

    def __contains__(self, key):
        return key in self.__items_name

    def __delitem__(self, key):
        idx = self.__items_name.index(key)
        self.__items_name.pop(idx)
        self.__num_of_item -= 1
        self.__items_index = list(range(self.__num_of_item))
        del self.__items[key]

    def __len__(self):
        return len(self.__items)


shopping_cart = Cart()

#############################################################################################
# __setitem__特殊方法實現單個及多個購物車添加
shopping_cart['購物車1'] = ['水']
shopping_cart['購物車1'] = ['好水']
shopping_cart[['購物車2', '購物車3']] = [['餅乾', '酒', '雞肉'], ['冰']]

print(shopping_cart, f'type= {type(shopping_cart)}')

###############################################################################################
# __getitem__特殊方法獲取單個及多個購物車內容
print('-'*30)
temp = shopping_cart['購物車1']
print(temp, f'type= {type(temp)}')

temp = shopping_cart[['購物車1', '購物車2']]
print(temp, f'type= {type(temp)}')

###############################################################################################
# 遍歷購物車
# it = iter(shopping_cart)
# print(next(it))
# print(next(it))
# print(next(it))
# 遍歷購物車
print('-'*30)
for cart in shopping_cart:
    print(cart, f'type= {type(cart)}')

###############################################################################################
# __contains__特殊方法 配合in關鍵字
print('-'*30)
print('購物車4' in shopping_cart)

###############################################################################################
# __delitem__特殊方法 配合del關鍵字
print('-'*30)
del shopping_cart['購物車1']
del shopping_cart['購物車3']
print(len(shopping_cart))
for cart in shopping_cart:
    print(cart, f'type= {type(cart)}')











# 練習: 定義一個Cart支援購物車的添加、移除及條件篩選
'''
class Cart(list):
    class CartCompareResult(list):
        def __repr__(self):
            text = '購物車中的比較結果\n'
            for i, item in enumerate(self):
                text += '物品{:2d}: {:s}\n'.format(i + 1, str(item))

            return text

    # def __len__(self):
    #     # 錯誤寫法
    #     # return len(self)
    #
    # def append(self, __object):
    #     super().append(__object)
    def __setitem__(self, key, value):
        if isinstance(key, int):
            if isinstance(value, list):
                raise Exception('input error')
            # key是整形時，附加至list
            self.append(value)
        else:
            # 切片賦值調用父類__setitem__方法
            super().__setitem__(key, value)

    def __getitem__(self, item):
        if isinstance(item, list):
           result = Cart()
           for i, valid in enumerate(item):
               if valid:
                   result.append(self[i])
           return result

        else:
           return super().__getitem__(item)

    def __repr__(self):
        text = '購物車中的內容\n'
        for i, item in enumerate(self):
            text += '物品{:2d}: {:s}\n'.format(i+1, str(item))

        return text

    # 運算符重載
    def __gt__(self, other):
        temp = Cart.CartCompareResult()
        for item in self:
            temp.append(item>other)
        return temp



shopping_cart = Cart()
shopping_cart.append(20)
# 打印購物車內容特殊方法__repr__
print(shopping_cart)

# 添加一個物品至購物車
# 定義__setitem__特殊方法
shopping_cart[1] = 5

# 添加多個物品至購物車
# 定義__setitem__特殊方法
shopping_cart[1:3] =  [10, 100]

# 刪除購物車內容
# 定義__delitem__特殊方法
# del shopping_cart[0:1]
# print(shopping_cart)

# 實現類似numpy中的布爾索引
print(shopping_cart>15)
print(shopping_cart[0])
print(shopping_cart[shopping_cart>15])
# print(shopping_cart[shopping_cart>15, ,])
# print(shopping_cart[2:0:-1])

# shopping_cart[slice([True, False, True])]

# for item in shopping_cart:
#     print(item)
'''
