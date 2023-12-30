hash_set = set()
for _ in range(int(input())):
    command, data = input().split()
    data = int(data)

    if command == 'add':
        hash_set.add(data)
    elif command == 'remove':
        hash_set.remove(data)
    else:
        print('true' if data in hash_set else 'false')