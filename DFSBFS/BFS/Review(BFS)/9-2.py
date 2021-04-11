#https://www.acmicpc.net/problem/5014
#백준 5014번 스타트링크(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque
def bfs(n):
    q = deque()
    q.append(n)
    while q:
        i= q.popleft()
        for j in direction:
            di = i+j
            if di < 0 or di >= f:
                continue
            elif i == g-1:
                print(apt[i]-1)
                return 
            elif apt[di] == 0:
                q.append(di)
                apt[di] = apt[i]+1
                
    print("use the stairs")
    return
   
                
    
f, s, g, u, d = map(int, input().split())
#f : 총 층, g : 목표, s : 현재 위치, u : 위로 u층, d : 아래로 d층

apt = [0]*f
apt[s-1] = 1
direction = [u,-d]
bfs(s-1)
'''
굳의 bfs를 값을 return하는 식으로 하지 않는 방식으로 바꾸고 초기 값을 int(1e9)가
아닌 0으로 하면 실행속도가 약 200ms정도 더 빨랐다. 다음부터 풀 때에는 염두하자
'''