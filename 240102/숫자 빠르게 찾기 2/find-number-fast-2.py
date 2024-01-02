from sortedcontainers import SortedSet
n, m = map(int, input().split())

s = SortedSet(list(map(int, input().split())))
len_s = len(s)


for _ in range(m):
    item = int(input())
    idx = s.bisect_left(item)
    if idx < len(s):
        print(s[idx])
    else:
        print(-1)