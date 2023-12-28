from collections import defaultdict

dic = dict()
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x not in dic or y < dic[x]:
        dic[x] = y

print(sum(dic.values()))