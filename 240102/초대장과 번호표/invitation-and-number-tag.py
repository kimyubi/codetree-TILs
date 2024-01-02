n, g = map(int, input().split())

invitation = set()
invitation.add(1)

for idx in range(g):
    data = list(map(int, input().split()))
    cnt, group = data[0], data[1:]
    
    diff = set(group) - invitation
    if len(diff) == 1:
        invitation.add(diff.pop())


print(len(invitation))