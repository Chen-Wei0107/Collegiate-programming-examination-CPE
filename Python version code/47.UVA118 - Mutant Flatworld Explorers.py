move = {
        'N': (0, 1),  # go up - N
        'S': (0, -1), # go down - S
        'E': (1, 0),  # go right - E
        'W': (-1, 0)  # go left - W
    }

falls = []

def turn(faces: str, direction: str) -> str:
    dirs = ['N', 'E', 'S', 'W']
    cur = dirs.index(faces)
    direction = 1 if direction == 'R' else -1
    
    if cur + direction < 0: return dirs[-1]
    if cur + direction > 3: return dirs[0]
    return dirs[cur + direction]

def solve(width, height, pos, faces, codes):
    # pos -> [x, y]
    for code in codes:
        if code == 'F':
            previous = [pos[0], pos[1]]
            pos[0] += move[faces][0]
            pos[1] += move[faces][1]

            if (pos[0] < 0 or pos[0] > width) or (pos[1] < 0 or pos[1] > height): # 判斷機器人是否超出邊界
                if previous in falls: # 機器人移動後超出了邊界，但是這個位置已經被紀錄過了，所以忽略此指令
                    pos[0], pos[1] = previous[0], previous[1] # 記得把機器人位置移到移動前的位置
                    continue

                falls.append(previous) # 紀錄掉下去之前的位置
                return f'{previous[0]} {previous[1]} {faces} LOST'
        else:
            faces = turn(faces, code)

    return f'{pos[0]} {pos[1]} {faces}'

width, height = list(map(int, input().split()))
while True:
    try:
        x, y, faces = input().split()
        codes = input().rstrip()

        print(solve(width, height, [int(x), int(y)], faces, codes))
    except EOFError:
        break