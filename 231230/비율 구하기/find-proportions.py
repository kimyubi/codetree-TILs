from sortedcontainers import SortedDict

dic = SortedDict()
n = int(input())
for _ in range(n):
    data = input()
    if data not in dic:
        dic[data] = 1
    else:
        dic[data] += 1

for key, value in dic.items():
    print(key,"{:.4f}".format(round(value/n * 100, 4)))