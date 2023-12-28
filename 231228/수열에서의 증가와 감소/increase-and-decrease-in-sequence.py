n = int(input())
data = list(map(int, input().split()))

dp_increase = [1] * n
dp_decrease = [1] * n

for i in range(n):
    for j in range(i):
        if data[j] <= data[i]:
            dp_increase[i]= max(dp_increase[j] + 1, dp_increase[i])

for i in range(n):
    for j in range(i):
        if data[i] <= data[j]:
            dp_decrease[i]= max(dp_decrease[j] + 1, dp_decrease[i])

print(max(max(dp_decrease), max(dp_increase)))