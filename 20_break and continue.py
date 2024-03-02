# break
# break可以用來立即退出循環語句(包括else)
# continue
# continue可以用來跳過當次循環
# break和continue都是只對離它最近的循環起作用

# pass
# pass是用來在判斷語句或循環語句中占位的

# 創建一個五次的循環
# break
i = 0
while i < 5:
    if i == 3:
        break
    print("i=", i)
    i += 1
else:
    print("循環結束")

# continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print("i=", i)

else:
    print("循環結束")

# pass
if i < 5:
    pass
