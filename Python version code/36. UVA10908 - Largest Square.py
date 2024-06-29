def square_check_per_size(arr, r, c, size):
    for i in range(r - size, r + size + 1):
        for j in range(c - size, c + size + 1):
            if i == r - size or i == r + size:
                if arr[i][j] != arr[r][c]:
                    return False
            elif j == c - size or j == c + size:
                if arr[i][j] != arr[r][c]:
                    return False
    return True

def main():
    T = int(input())
    for _ in range(T):
        M, N, Q = map(int, input().split())
        arr = [list(input()) for _ in range(M)]

        print(M, N, Q)

        for _ in range(Q):
            r, c = map(int, input().split())
            size = 1

            while (r - size >= 0) and (r + size < M) and (c - size >= 0) and (c + size < N) and square_check_per_size(arr, r, c, size):
                size += 1

            size -= 1
            print(size * 2 + 1)

if __name__ == "__main__":
    main()
