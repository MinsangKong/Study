#https://www.acmicpc.net/problem/2668
#백준 2668번 숫자 고르기(DFS)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(3000000)

def dfs(n,i):
    visited[n] = 1
    for j in board[n]:
        if visited[j] == 0:
            dfs(j,i)
        elif visited[j] == 1 and j==i:
            result.append(j)
            
n = int(input())
board = [[] for i in range(n+1)]
for i in range(n):
    board[i+1].append(int(input()))
    
result = []
for i in range(1, n+1):
    visited = [0] * (n+1)
    dfs(i,i)
            
print(len(result))
for i in result:
    print(i)
    
'''
문제를 잘못 이해해서 엄청 해맸다. 서로 연결되었다는 뜻은 바로 싸이클이 발생한다는
소리이기 때문에 사이클을 발생시키는 i값만 result에 추가하면 되는 문제였다.

'''