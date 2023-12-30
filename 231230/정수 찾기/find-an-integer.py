n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

c = set(b)-set(a)

for x in b:
    print(1 if x not in c else 0)