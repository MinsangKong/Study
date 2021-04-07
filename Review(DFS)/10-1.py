#https://www.acmicpc.net/problem/1987
#백준 1987번 알파벳(DFS)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(300000)

def dfs(x, y, check):  
    global result
    if result < len(check):
        result = len(check)
    for a,b in direction:
        dx = x+a
        dy = y+b
        if dx < 0 or dx >=r or dy < 0 or dy >=c:
            continue
        else:
            if word[dx][dy] not in check:
                dfs(dx,dy,check+word[dx][dy])

r, c = map(int, input().split())
word = []

for _ in range(r):
    word.append(input())
    
result = 0
check=word[0][0]
direction = [(1,0),(-1,0),(0,1),(0,-1)]
dfs(0,0,check)

print(result)

'''
가장 빠르게 푸는 방법은 생각했던 대로 BFS를 활용하는 방식이었다. 더 빠르게 풀려면
알파벳 26가지를 가지고 있는 배열을 만든 뒤 해당 글자가 나오면 1을 더하는 방식으로
한 뒤 in 문법을 안 썼으면 더 빨랐을 것 같다.
'''