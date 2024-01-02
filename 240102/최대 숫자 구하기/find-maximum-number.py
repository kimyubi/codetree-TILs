from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = SortedSet([i for i in range(1, m + 1)])

data = list(map(int, input().split()))
for x in data:
    arr.remove(x)
    print(arr[-1])