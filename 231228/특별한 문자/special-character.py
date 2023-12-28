from collections import Counter
data = input().rstrip()
counter = Counter(data)

exist = False
for x in data:
    if counter[x] == 1:
        print(x)
        exist = True

if not exist:
    print(None)