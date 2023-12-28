from collections import defaultdict
n, k = map(int, input().split())
data = list(map(int, input().split()))
ans = 0
for i in range(2, n):
    target = k - data[i]
    dic = defaultdict(int)
    for j in range(i):
        diff = target - data[j]
        ans += dic[diff]
        dic[data[j]] += 1

print(ans)