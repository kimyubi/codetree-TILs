# from collections import Counter
# n = int(input())
# data = [input() for _ in range(n)]
# counter = Counter(data)
# print(counter.most_common(1)[0][1])


from collections import defaultdict
n = int(input())
dic = defaultdict(int)
for _ in range(n):
    dic[input()] += 1

print(max(dic.values()))