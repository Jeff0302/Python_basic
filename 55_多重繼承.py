class A(object):
    def test(self):
        print('AAA')

    def test2(self):
        print('A_BBB')

class B(object):
    def test2(self):
        print('BBB')

# 在Python中是支持多重繼承的，也就是我們可以為一個類同時指定多個父類
#  可以在類名中的()添加多個類，來實現多重繼承
#  多重繼承，會使子類同時擁有多個父類，並且會獲取到父類中所有方法
# 在開發中沒有特殊情況，應該盡量避免使用多重繼承，因為多重繼承會讓代碼過於複雜
# 如果多個父類中有同名的方法，則會在第一個父類中尋找，如果有則使用
#   如果沒有則會往下面的父類尋找，依此類推，如果都沒找到則會報錯

# C(A, B) 、 C(B, A)
class C(A, B):
    def test3(self):
        print('CCC')


# __bases__ 這個屬性可以用來獲取當前類的所有父類
c = C()
c.test2()
print(C.__bases__)