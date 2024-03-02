# 在對集合做運算時，不會影響原來的集合，而返回一個運算結果
# 創建兩個集合
s = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

# & 交集運算
result = s & s2
print(result)

# | 並集運算
result = s | s2
print(result)

# - 差集
# result = s - s2
result = s2 - s
print(result)

# ^ 亦或集(獲取不相交部分, 獲取只在一個集合出現的元素)
result = s ^ s2
print(result)

# <= 檢查一個集合是否是另一個集合的子集
# 如果a集合中的元素全部在b集合中出現，那麼a集合就是b集合的子集，b集合就是a集合的超集
s3 = {1, 2, 3}
result = s3 <= s
print(result)

# <= 檢查一個集合是否是另一個集合的子集
# 如果超集b中含有子集a中的所有元素，並且b中還有a中沒有的元素，則b就是a的真超集，a為b的真子集
result = {1, 2, 3} < {1, 2, 3}
print(result)

# >= 檢查一個集合是否是另一個集合的超集
# > 檢查一個集合是否是另一個集合的真超集
