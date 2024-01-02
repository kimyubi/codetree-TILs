from sortedcontainers import SortedSet

for _ in range(int(input())):
    s = SortedSet()

    for i in range(int(input())):
        command, x = input().split()
        x = int(x)

        if command == "I":
            s.add(x)
        
        else:
            if not s:
                continue

            if x == 1:
                s.remove(s[-1])
            else:
                s.remove(s[0])

    if not s:
        print('EMPTY')
    else:
        print(s[-1], s[0])