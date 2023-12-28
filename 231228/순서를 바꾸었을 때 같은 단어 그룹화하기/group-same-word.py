from collections import defaultdict

dic = defaultdict(int)
for _ in range(int(input())):
    dic[''.join(sorted(list(input().rstrip())))] += 1
    
print(max(dic.values()))