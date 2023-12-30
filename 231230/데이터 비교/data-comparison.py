n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

for x in arr2:
    print(1 if x in arr1 else 0, end =' ')