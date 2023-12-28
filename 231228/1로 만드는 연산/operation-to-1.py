import sys
ans = sys.maxsize

def solution(depth, n):
    global ans
    if n <= 1:
        ans = min(ans, depth)
        return

    if not n % 3:
        solution(depth + 1, n // 3)
    
    if not n % 2:
        solution(depth + 1, n // 2)
    
    solution(depth + 1, n-1)

n = int(input())
solution(0, n)
print(ans)