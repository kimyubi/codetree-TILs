from sortedcontainers import SortedSet

s = SortedSet()
for _ in range(int(input())):
    command = input()

    if command == 'largest':
        if not s:
            print(None)
        else:
            print(s[-1])
        continue
    
    if command == 'smallest':
        if not s:
            print(None)
        else:
            print(s[0])
        continue

    c, x = command.split()[0], command.split()[1]
    x = int(x)
    
    if c == 'add':
        s.add(x)
    
    if c == 'remove':
        s.remove(x)

    if c == 'find':
        print("true" if x in s else "false")
    
    if c == 'lower_bound':
        idx = s.bisect_left(x)
        
        if idx < len(s):
            print(s[idx])
        else:
            print("None")

    if c == 'upper_bound':
        idx = s.bisect_right(x)

        if idx < len(s):
            print(s[idx])
        else:
            print("None")