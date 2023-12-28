from collections import defaultdict

# 원소의 개수 n, 두 수의 합이 될 k
n, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

s, e = 0, n-1
ans = 0
while s < e:
    sum_two = data[s] + data[e]
    if sum_two == k:
        ans += 1
        s += 1
    elif sum_two < k:
        s += 1
    else:
        e -= 1

print(ans)