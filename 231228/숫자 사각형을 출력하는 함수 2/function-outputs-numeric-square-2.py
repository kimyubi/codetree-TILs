n = int(input())
ans = [[0] * n for _ in range(n)]

for i in range(n):
    ans[i][0] = i + 1
    for j in range(1, n):
        ans[i][j] = ans[i][j-1] * 2

for row in ans:
    print(*row)