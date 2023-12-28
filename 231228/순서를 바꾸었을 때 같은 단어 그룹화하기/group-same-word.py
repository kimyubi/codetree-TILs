from collections import defaultdict

dic = defaultdict(int)
for _ in range(int(input())):
    dic[''.join(sorted(list(input().rstrip())))] += 1
    
ans = sorted(list(dic.items()), key = lambda x : -x[1])
print(ans[0][1])