from sortedcontainers import SortedSet

s = SortedSet()
n, m = map(int, input().split())

for _ in range(n):
    x, y = map(int, input().split())
    s.add((x, y))

len_s = len(s)
for _ in range(m):
    i, j = map(int, input().split())
    idx = s.bisect_left((i, j))

    if idx < len_s:
        print(*s[idx])
    
    else:
        print(-1, -1)