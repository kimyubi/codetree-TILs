import sys

input = sys.stdin.readline
n = int(input())
dic = dict()

for _ in range(n):
    data = input().split()
    command = data[0]

    if command == 'add':
        k, v = int(data[1]), int(data[2])
        dic[k] = v

    elif command == 'remove':
        k = int(data[1])
        dic.pop(k)
    
    else:
        k = int(data[1])
        print(dic[k] if k in dic else None)