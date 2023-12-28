from collections import defaultdict

# 원소의 개수 n, 두 수의 합이 될 k
n, k = map(int, input().split())
data = list(map(int, input().split()))
dic = defaultdict(int)

for i in range(n):
    for j in range(i+1, n):
        dic[data[i] + data[j]] += 1


print(dic[k])