#https://www.acmicpc.net/problem/2310
#백준 2310번 어드벤처 게임(DFS)
import sys
#input = sys.stdin.readline
result = []
while True:
    n = int(input())
    room = []
    visited = [False] * n
    cnt = 0
    if n == 0:
        break
    for i in range(n):
        room.append(list(input().split()))
    def dfs(i, cnt):
        if room[i][0] == "E":
            visited[i] = True
            for j in range(2, len(room[i])-1):
                if not visited[int(room[i][j])-1] :
                    dfs(int(room[i][j])-1, cnt)
        elif room[i][0] == "L":
            visited[i] = True
            if cnt < int(room[i][1]):
                cnt = int(room[i][1])
            for j in range(2, len(room[i])-1):
                if not visited[int(room[i][j])-1]:
                    dfs(int(room[i][j])-1, cnt)
        elif room[i][0] == "T" and cnt >= int(room[i][1]):
            visited[i] = True
            cnt-=int(room[i][1])
            for j in range(2, len(room[i])-1):
                if not visited[int(room[i][j])-1]:
                    dfs(int(room[i][j])-1, cnt)
    
    dfs(0,0)
    if visited[n-1]:
        result.append("Yes")
    else:
        result.append("No")
                
for i in result:
    print(i)