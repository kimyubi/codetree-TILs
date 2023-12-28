from collections import defaultdict

n = int(input())
data = [list(map(int, input().split())) for _ in range(4)]
ans = 0

dic = defaultdict(int)
for a in data[0]:
    for b in data[1]:
        dic[a + b] += 1

for c in data[2]:
    for d in data[3]:
        target = -(c + d)
        ans += dic[target]

print(ans)