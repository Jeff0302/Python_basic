# 創建一個列表
stus = ['孫悟空', '豬八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']

# 修改列表中的元素
# 直接通過索引來修改元素
print('修改前:', stus)
stus[0] = 'sunwukong'
print('修改後:', stus)

# 通過del來刪除元素
del stus[1]
print('修改後:', stus)

stus = ['孫悟空', '豬八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']
# 通過切片修改列表
#   在給切片賦值時，只能使用序列 TypeError: can only assign an iterable
# stus[0:1] = 123
# stus[0:3] = ['孫悟空2', '豬八戒2', '二郎神']   # 使用新的元素替換舊元素
# stus[0:1] = ['牛魔王']     # 向索引為0位置插入元素
# 當設置步長時，序列中的元素個數必須和切片的元素個數一致
stus[::2] = ['豬八戒2', '沙和尚2', '唐僧2']
print('修改後:', stus)

# 也可以通過切片來刪除元素
# del stus[1:3]
# del stus[::2]
stus[1:3] = []
print('修改後:', stus)

# 以上操作只是適用於可變序列
s = 'hello'
# s[0] = 'a' 不可變序列，無法通過索引來修改
# 可以通過list()函數將其他序列轉換為list
s = list(s)
s[0] = 'a'
# import functools
# print(functools.reduce(lambda x, y: x+y, s))






