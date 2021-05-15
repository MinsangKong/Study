#Q19 연산자 끼워 넣기
#import sys
#input = sys.stdin.readline
from collections import deque
def bfs(length):
    q = deque()
    q.append((oper[0],oper[1],oper[2],oper[3],num[0],1))
    while q:
        plus, minus, mul, div, n, cnt = q.popleft()
        if cnt == length:
            result.append(n)
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
result = []
length = len(num)

bfs(length)

print(max(result))
print(min(result))
'''
속도면에서는 max와 min함수를 사용하지 않고 최댓값과 최솟값을 미리 지정한 다음에 갱신하는
방식보다 result를 활용한 방식이 의외로 빨랐다. 더 빠르게 풀기 위해서는 dfs로 각각
if문을 적용하는 방식을 활용해야 한다.
제일 빠르게 푸는 방식은 중복순열을 활용해서 문제를 푸는 방식이다.
from itertools import product
n = 4
print(list(product([‘+’, ‘-’, ‘*’, ‘/’], repeat= (n - 1))))
'''