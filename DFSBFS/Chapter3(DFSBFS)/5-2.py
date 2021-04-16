#import sys
#input = sys.stdin.readline
from collections import deque
def bfs(length):
    global minV, maxV
    q = deque()
    q.append((oper[0],oper[1],oper[2],oper[3],num[0],1))
    while q:
        plus, minus, mul, div, n, cnt = q.popleft()
        if cnt == length:
            minV = n if n < minV else minV
            maxV = n if n > maxV else maxV
        if plus > 0 :
            q.append((plus-1,minus,mul,div,n+num[cnt],cnt+1))
        if minus > 0:
            q.append((plus,minus-1,mul,div,n-num[cnt],cnt+1))
        if mul > 0 :
            q.append((plus,minus,mul-1,div,n*num[cnt],cnt+1))
        if div > 0 :
            if n < 0:
                a = -(-n//num[cnt])
                q.append((plus,minus,mul,div-1,a,cnt+1))
            else:
                q.append((plus,minus,mul,div-1,n//num[cnt],cnt+1))

n = int(input())
num = list(map(int, input().split()))
oper = list(map(int, input().split()))
minV = 987654321
maxV = -987654321
length = len(num)

bfs(length)

print(maxV)
print(minV)