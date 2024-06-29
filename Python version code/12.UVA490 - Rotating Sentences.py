lines = []

while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break  # 當遇到 EOFError 時結束循環

# 找出最長的行的長度
max_length = max(len(line) for line in lines)

newlines = []

# 將輸入的行進行逆序，以實現逆時針旋轉
for i in range(len(lines) - 1, -1, -1):
    newlines.append(lines[i])

rotated_lines = []

# 遍歷每一列，將其旋轉90度並添加到 rotated_lines 中
for i in range(max_length):
    rotated_line = ''
    for line in newlines:
        if i < len(line):
            rotated_line = rotated_line + line[i]
        else:
            if line != newlines[-1]:
                rotated_line = rotated_line + ' '
    rotated_lines.append(rotated_line)

# 輸出旋轉後的文本
for line in rotated_lines:
    print(line)
