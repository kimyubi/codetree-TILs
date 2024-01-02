from itertools import combinations 

n, m = map(int, input().split())

group_a = [list(input()) for _ in range(n)]
group_b = [list(input()) for _ in range(n)]
arr = [i for i in range(m)]

ans = 0
for x, y, z in combinations(arr, 3):
    dedicate_a = []
    for row in group_a:
        dedicate_a.append((row[x], row[y], row[z]))

    dedicate_b = []
    for row in group_b:
        dedicate_b.append((row[x], row[y], row[z]))

    dedicate_a, dedicate_b = set(dedicate_a), set(dedicate_b)
    
    if not (dedicate_a & dedicate_b):
        ans += 1

    
print(ans)