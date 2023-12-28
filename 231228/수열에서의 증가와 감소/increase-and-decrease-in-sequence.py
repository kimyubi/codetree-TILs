n = int(input())
data = list(map(int, input().split()))

ans = 0

tmp = 1
for i in range(1, n):
    if data[i-1] <= data[i]:
        tmp += 1
    else:
        ans = max(ans, tmp) 
        tmp = 1
ans = max(ans, tmp) 

tmp = 1
for i in range(1, n):
    if data[i-1] >= data[i]:
        tmp += 1
    else:
        ans = max(ans, tmp) 
        tmp = 1
ans = max(ans, tmp) 

print(ans)