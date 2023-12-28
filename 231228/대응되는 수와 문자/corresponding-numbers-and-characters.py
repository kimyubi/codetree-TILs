import sys

dic = dict()
input = sys.stdin.readline
# 숫자의 개수 n, 조사할 값의 개수 m
n, m = map(int, input().split())
data = [input().rstrip() for _ in range(n)]

for idx, v in enumerate(data):
    dic[idx + 1] = v
    dic[v] = idx + 1

query = [input().rstrip() for _ in range(m)]
for q in query:
    if q.isdigit():
        q = int(q)
    print(dic[q])