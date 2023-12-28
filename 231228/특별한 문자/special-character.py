from collections import Counter
data = input().rstrip()
counter = Counter(data)

def solution():
    for x in data:
        if counter[x] == 1:
            return x
    return None

print(solution())