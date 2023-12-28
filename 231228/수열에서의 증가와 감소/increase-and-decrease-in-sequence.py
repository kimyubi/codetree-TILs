n = int(input())
data = list(map(int, input().split()))

ans1 = 0
ans2 = 0

tmp1 = 1
for i in range(1, n):
    if data[i-1] <= data[i]:
        tmp1 += 1
    else:
        ans1 = max(ans1, tmp1) 
        tmp1 = 1
ans1 = max(ans1, tmp1) 

tmp2 = 1
for i in range(1, n):
    if data[i-1] >= data[i]:
        tmp2 += 1
    else:
        ans2 = max(ans2, tmp2) 
        tmp2 = 1
ans2 = max(ans2, tmp2) 

print(max(ans1, ans2))