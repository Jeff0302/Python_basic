# 文件(File)
#   - 通過Python程序來對計算機中的各種文件進行增刪改查的操作
#   - I/O(Input/Output)
#   - 操作文件的步驟
#     1. 打開文件
#     2. 對文件進行各種操作(讀、寫)，然後保存
#     3. 關閉文件

# open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# 使用open函數來打開文件
# 參數:
#       file = 要打開文件的名字(路徑)
# 返回值:
#       返回一個對象，這個對象代表當前打開的文件


# 創建一個變量，來保存文件的名字
file_name = 'demo.txt'

# 在window系統使用路徑時，可以使用/來代替\
# 或者可以使用\\來代替\
# 或者也可以使用原始字符串r'.....'

# 表示路徑可以使用..來返回一級目錄

# 如果目標文件距離當前文件比較遠，此時可以使用絕對路徑
# 絕對路徑應該從磁盤的根目錄開始書寫
try:
    # 調用open()打開文件
    # 當我們獲取了文件對象以後，所有的文件操作都會通過該對象向來進行
    f = open('demo.txt')
    print(f)
except:
    print('文件打開失敗')
else:
    # 讀取文件中的內容
    # read()方法，用來讀取文件中的內容，它會將內容全部保存為一個字符串
    result = f.read()
    print(result)
    # 關閉文件
    # 調用close()方法來關閉文件
    f.close()

# with ... as 語句
with open('demo.txt') as file:
    # 在with語句中可以直接使用文件對象來做文件操作
    # 此時這個文件只能在with中使用，一旦with結束則文件自動close()
    print(file.read())

file_name = 'demo.txt'
try:
    with open(file_name) as file_obj:
        print(file_obj.read())
except FileNotFoundError:
    print(f'{file_name} 文件不存在~~')


