quote = True  # 初始化引號打開的狀態為 True，表示下一個引號是左尖括號

while True:
    try:
        line = input()  # 讀取一行文本
        result = ''  # 用於存儲處理後的結果

        for char in line:
            if char == '"':
                if quote:
                    result += '``'  # 如果引號打開，則替換為左尖括號
                else:
                    result += "''"  # 如果引號關閉，則替換為右尖括號
                quote = not quote  # 切換引號的狀態
            else:
                result += char  # 其他字符保持不變

        print(result)  # 輸出處理後的結果

    except EOFError:
        break  # 當遇到 EOFError 時結束循環
