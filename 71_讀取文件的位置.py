with open('demo.txt', mode='rt', encoding='utf-8') as file_obj:
    # seek() 可以修改當前讀取位置
    # seek() 需要兩個參數
    #   1. 第一個是要切換的位置
    #   2. 計算位置方式
    #           可選值:
    #               0 從頭計算， 默認值
    #               1 從當前位置計算
    #               2 從最後位置開始計算
    file_obj.seek(9)
    # file_obj.seek(80, 0)
    # file_obj.seek(70, 1)
    # file_obj.seek(-10, 2)
    # print(file_obj.read(100))
    # print(file_obj.read(30))
    # tell() 方法查看當前讀取位置
    print('當前讀取到了 --> ', file_obj.tell())