from sortedcontainers import SortedDict

dic = SortedDict()

for _ in range(int(input())):
    data = input()
    if 'add' in data:
        command, a, b = data.split()
        a, b = int(a), int(b)
        dic[a] = b
    
    elif 'remove' in data:
        command, a = data.split()
        a = int(a)
        dic.pop(a)


    elif 'find' in data:
        command, a = data.split()
        a = int(a)
        print(dic[a] if a in dic else None)
    
    else:
        if not dic:
            print(None)

        else:
            for value in dic.values():
                print(value, end = ' ')
            print()