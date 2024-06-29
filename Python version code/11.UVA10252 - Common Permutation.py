while True:  # 進入無限循環
    word0 = list(input())  # 讀取第一個單詞並將其轉換為字母列表
    word1 = list(input())  # 讀取第二個單詞並將其轉換為字母列表
    ans = []  # 用於存儲共同出現的字母

    # 遍歷第一個單詞中的不重複字母
    for i in set(word0):
        # 檢查字母是否也出現在第二個單詞中，並且是字母而不是其他字符
        if i in word1 and i.isalpha():
            # 將重複的字母添加到 ans 列表中，次數等於兩個單詞中出現次數較少的次數
            ans.append(i * min(word0.count(i), word1.count(i)))

    ans.sort()  # 將 ans 列表按字母順序排序

    for i in ans:
        print(i, end="")  # 輸出共同出現的字母
    print()  # 換行以處理下一組輸入
