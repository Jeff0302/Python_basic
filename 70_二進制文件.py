file_name = 'test.xlsx'
#  讀取模式
"""
    t   讀取文本文件(默認值)
    b   讀取二進制文件
"""


with open(file_name, mode='rb') as file_name:
    # 讀取文本文件時，size是以字符為單位
    # 讀取二進制文件時，size是以字節byte為單位
    # print(file_name.read(10))

    # 將讀取到的內容寫出來
    # 定義一個新的文件
    new_name = 'test_copy.xlsx'
    with open(new_name, mode='wb') as new_file:
        # 定義每次讀取的大小
        chunk = 1024*100
        while True:
            # 從已有的對象中讀取數據
            temp = file_name.read(chunk)
            if not temp:
                break
            # 將讀取到的數據寫入新的對象中
            new_file.write(temp)
