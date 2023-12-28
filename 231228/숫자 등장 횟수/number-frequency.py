from collections import Counter
import sys
input = sys.stdin.readline

# 원소의 개수 n, 질의의 개수 m
n, m = map(int, input().split())
data = list(map(int, input().split()))
couter = Counter(data)

for num in list(map(int, input().split())):
    print(couter[num], end = ' ')