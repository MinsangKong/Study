#https://www.acmicpc.net/problem/2210
#백준 2210번 숫자판 점프(DFS)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(3000000)

def dfs(x, y, num):
    if len(num) == 6 and int(num) not in result :
        result[int(num)] = 1
    else:
        for a, b in direction:
            dx = x+a
            dy = y+b
            if dx < 0 or dx >=5 or dy < 0 or dy >=5:
                continue
            else:
                if(len(num) < 6):
                    dfs(dx, dy, num+board[dx][dy])
                    
board = []
result = {}
direction = [(1,0),(-1,0), (0,1), (0,-1)]
for i in range(5):
    board.append(input().split())
    
for i in range(5):
    for j in range(5):
        num = ""
        for a,b in direction:
            dx = i+a
            dy = j+b
            if dx < 0 or dx >= 5 or dy < 0 or dy >=5:
                continue
            else:
                dfs(dx, dy, board[dx][dy]+num)

print(len(result))
'''
다 풀고 남의 소스 코드를 보니까 dictionary를 쓰는 것보다 set을 사용했으면 속도면에서
훨씬 빨랐을 것이다. dictionary를 사용한 코드에서는 중복을 체크하는 if문을 처리해야 했기
때문에 경우의 수가 많은 문제에선 비효율적이었다. 앞으로는 set을 기억하자
'''