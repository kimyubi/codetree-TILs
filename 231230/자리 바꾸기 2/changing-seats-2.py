from collections import defaultdict
dic = defaultdict(set)
[0, 1, 4, 2, 3, 5]
n, k = map(int, input().split())
position = [i for i in range(n + 1)]
data = [list(map(int, input().split())) for _ in range(k)]

for i in range(1, n + 1):
    dic[i].add(i)

for _ in range(3):
    for a, b in data:
        dic[position[a]].add(b)
        dic[position[b]].add(a)

        position[a], position[b] = position[b], position[a]

for i in range(1, n + 1):
    print(len(dic[i]))