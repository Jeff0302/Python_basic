# 條件運算符(三元運算符)
# 語法: 語句1 if 條件表達式 else 語句2
# 執行流程:
# 條件運算符在執行時，會先對條件表達式進行判斷
#   如果判定結果為true，則執行語句1，並返回執行結果
#   如果判定結果為false，則執行語句2，並返回執行結果

# print("你好") if True else print("Hello")
a = 10
b = 20
# print('a的值比較大') if a > b else print('a的值比較小')
max = a if a > b else b
print(max)