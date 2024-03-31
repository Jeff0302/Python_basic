file_name = 'demo.txt'

# 使用open()打開文件時必須要指定打開文件所要做的操作(讀、寫、追加)
# 如果不指定操作類型，則默認是讀取，而讀取文件時是不能向文件寫入的
"""
  r   表示只讀的
  w   表示可寫的，使用w寫入文件時，如果文件不存在會創建文件，如果存在會覆蓋原文件
  a   表示追加內容，如果文件不存在則會創建文件，如果文件存在則會將新內容追加到文件後面
  x   用來新建文件，如果文件不存在則創建，文件存在則報錯
  +   為操作符增加功能
  r+  可讀可寫。但文件不存在會報錯
  w+  可讀可寫，如果文件不存在會創建文件，如果存在會覆蓋原文件
  a+  可讀可寫，如果文件不存在則會創建文件，如果文件存在則會將新內容追加到文件後面
"""
with open(file_name, mode='a', encoding='utf-8') as file_obj:
    # write() 來向文件中寫入內容
    # 如果操作的是文本文件，write中需要傳遞一個字符串參數
    # 該方法可以分多次向文件寫入內容
    # 寫入完成以後，該方法會返回寫入的字符串個數
    file_obj.write('Hello Hello how are you1?'+'\n')
    file_obj.write('Hello Hello how are you2?'+'\n')
    r = file_obj.write(str(123)+'\n')
    print(r)