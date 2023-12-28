from collections import Counter
n = int(input())
data = [input() for _ in range(n)]
counter = Counter(data)
print(counter.most_common(1)[0][1])