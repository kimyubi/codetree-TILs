from itertools import combinations 

n, m = map(int, input().split())

group_a = [list(input()) for _ in range(n)]
group_b = [list(input()) for _ in range(n)]
comb = combinations([i for i in range(m)], 3)

ans = 0
for x, y, z in comb:
    dedicate_a = set()
    for row in group_a:
        dedicate_a.add((row[x], row[y], row[z]))

    dedicate_b = set()
    for row in group_b:
        dedicate_b.add((row[x], row[y], row[z]))

    if not (dedicate_a & dedicate_b):
        ans += 1

    
print(ans)