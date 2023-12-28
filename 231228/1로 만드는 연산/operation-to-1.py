n = int(input())
cnt = 0

while True:
    if n == 1:
        print(cnt)
        break
    
    if not n % 3:
        n //= 3
        cnt += 1
        continue
    
    if not n % 2:
        n //= 2
        cnt += 1
        continue
    
    n -= 1
    cnt += 1