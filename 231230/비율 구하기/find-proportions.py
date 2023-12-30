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
    ratio = value / n * 100

    # 소숫점 4째짜리까지만 출력합니다.
    print(f"{key} {ratio:.4f}")