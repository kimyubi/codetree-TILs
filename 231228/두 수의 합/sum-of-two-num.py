from collections import defaultdict

# 원소의 개수 n, 두 수의 합이 될 k
n, k = map(int, input().split())

data = list(map(int, input().split()))
dic = defaultdict(int)
ans = 0

for v in data:
    ans += dic[k - v]
    dic[v] += 1

print(ans)