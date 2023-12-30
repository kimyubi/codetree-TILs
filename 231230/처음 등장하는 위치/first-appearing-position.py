from sortedcontainers import SortedDict

dic = SortedDict()
n = int(input())
data = list(map(int, input().split()))

for idx, value in enumerate(data):
    if value not in dic:
        dic[value] = idx + 1

for key, value in dic.items():
    print(key, value)