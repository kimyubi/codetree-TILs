n, m = map(int, input().split())
set_1 = set(list(map(int,input().split())))
set_2 = set(list(map(int,input().split())))


print(len((set_1 - set_2) | (set_2-set_1)))