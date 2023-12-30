from sortedcontainers import SortedDict

dic = SortedDict()
for _ in range(int(input())):
    data = input()
    if data not in dic:
        dic[data] = 1
    else:
        dic[data] += 1


for key, value in dic.items():
    print(key, value)