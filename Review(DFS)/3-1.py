#https://www.acmicpc.net/problem/1325
#백준 1325번 효율적인 해킹(DFS)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(3000000)

def dfs(a):
    visited[a] = 1
    for j in range(a+1, n):
        if visited[j] == 0 and arr[a][j] == 1:
            dfs(j)
    
    
n, m = map(int, input().split())
arr = [[0]*n for _ in range(n)]

result = []

for i in range(m):
    a, b = map(int, input().split())
    arr[b-1][a-1] = 1

for i in range(n):
    visited = [0]*n
    dfs(i)
    result.append(visited.count(1))

for i in range(n):
    if result[i] == max(result):
        print(i+1, end=' ')
'''
거지 같은 문제 ㅡㅡ. dfs로 분류되어 있으면서 정작 dfs로 풀면 메모리초과가 발생한다.
'''