from collections import defaultdict
dic = defaultdict(int)

def solution(n):
    global dic
    if not n:
        dic[n] += 1
        return 0
    elif n == 1:
        dic[n] += 1
        return 1
    else:
        return solution(n-1) + solution(n-2)

n = int(input())
solution(n)
print(dic[0], dic[1])