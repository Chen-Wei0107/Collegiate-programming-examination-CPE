row1 = "qwertyuiop[]"
row2 = "asdfghjkl;'"
row3 = "zxcvbnm,./"

# 定義一個函數，將字母向左平移一個位置
def moverow(row, x):
    for i in range(len(row)):
        if x == row[i]:
            print(row[i - 2], end="")  # 輸出向左平移一個位置的字母


while True:  # 遍歷每個測試案例
    word = input()  # 讀取輸入的單詞

    for i in word.lower():  # 將單詞轉換為小寫字母，遍歷每個字母
        if i != " ":  # 忽略空格
            moverow(row1, i)  # 處理第一行的字母
            moverow(row2, i)  # 處理第二行的字母
            moverow(row3, i)  # 處理第三行的字母
        else:
            print(" ", end="")  # 輸出空格

    print()  # 換行，處理下一個測試案例

"""
row1="qwertyuiop[]"
row2="asdfghjkl;'"
row3="zxcvbnm,./"
def moverow(row,x):
    for i in range(len(row)):
        if (x == row[i]):
            print(row[(i-2)],end="")
while 1:
	word=input()
	for i in word.lower():
	    if i !=" ":
	        moverow(row1,i)
	        moverow(row2,i)
	        moverow(row3,i)
	    else:
	        print(" ",end="")
	print()
"""
"""用字典
key = { '2':'`', '3':'1', '4':'2', '5':'3', '6':'4', '7':'5', '8':'6', '9':'7', '0':'8', '-':'9', '=':'0',
		'e':'q', 'r':'w', 't':'e', 'y':'r', 'u':'t', 'i':'y', 'o':'u', 'p':'i', '[':'o', ']':'p', '\\':'[',
		'd':'a', 'f':'s', 'g':'d', 'h':'f', 'j':'g', 'k':'h', 'l':'j', ';':'k', '\'':'l',
		'c':'z', 'v':'x', 'b':'c', 'n':'v', 'm':'b', ',':'n', '.':'m', '/':','}
T=int(input())
for _ in range(T):
    word=input()
    for i in list(word.lower()):
        if i !=" ":
            print(key[i],end="")
        else:
            print(" ",end="")
"""  