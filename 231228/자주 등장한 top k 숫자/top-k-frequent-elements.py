from collections import Counter

n, k = map(int, input().split())
data = list(map(int, input().split()))

counter = list(Counter(data).items())
counter.sort(key = lambda x : (-x[1], -x[0]))
for key, value in counter[0:k]:
    print(key, end = ' ')