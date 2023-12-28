from collections import defaultdict

n = int(input())
data = [list(map(int, input().split())) for _ in range(4)]

dic_1 = defaultdict(int)
for a in data[0]:
    for b in data[1]:
        dic_1[a + b] += 1

dic_2 = defaultdict(int)
for c in data[2]:
    for d in data[3]:
        dic_2[c + d] += 1

ans = 0
for key, value in dic_1.items():
    ans += value * dic_2[-key]
print(ans)