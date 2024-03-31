file_name = 'demo.txt'

try:
    # 調用open()來打開文件，可以將文件分為兩種類型
    # 1. 純文本文件(使用utf-8等編碼編寫的文本文件)
    # 2. 二進制文件(圖片、mp3、ppt等這些文件)
    # open()打開文件時，默認是以文本文件的形式來打開，但是open()默認的編碼為None
    #  所以處理文本文件時，必需要指定文件的編碼
    #  如果直接調用read()它會將文件的所有內容讀取出來
    #    如果要讀取的文件較大的話，會一次性將文件的內容加載到內存中，容易造成內存洩漏
    #    所以對於較大的文件，不要直接調用read()

    #  read()可以接受一個size作為參數，該參數可以用來指定要讀取的字符數量
    #    默認值為-1，它會讀取文件中的所有字符
    #    可以為size指定一個值，這樣read()會讀取指定數量的字符串
    #       每一次讀取都是從上一次讀取到的位置開始
    #       如果字符數量小於size，則會讀取剩餘所有的
    #       如果已經讀取到最後了，則會返回空串''

    with open(file_name, encoding='utf-8') as file_obj:
        # 定義一個變量保存文件內容
        temp = ''
        # 定義一個變量，來指定每次讀取的大小
        chunk = 100
        # 創建一個循環來讀取文件內容
        while True:
            # 讀取chunk大小的內容
            content = file_obj.read(chunk)

            if not content:
                # 內容讀取完畢，跳出循環
                break
            # 輸出內容
            temp += content

except FileNotFoundError:
    print(f'{file_name} 文件不存在~~')

else:
    print(temp)


# readline()及readlines()方法
with open(file_name, encoding='utf-8') as file_obj:
    # readline()
    # 該方法可以用來讀取一行內容
    # print(file_obj.readline(), end='')
    # print(file_obj.readline(), end='')
    # readlines()
    # 該方法用於一行一行的讀取內容，它會一次性將讀取到的內容封裝到一個列表中並返回
    # print(file_obj.readlines())
    # print('*****************')
    for t in file_obj:
        print(t)
