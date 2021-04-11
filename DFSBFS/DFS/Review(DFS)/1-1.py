#https://www.acmicpc.net/problem/19621
#백준 19621번 회의실 배정 2(DFS)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(3000000)

def dfs(i,cnt):
    cnt += room[i][2]
    if room[i][1] > goal:
        result.append(cnt)
    for j in range(i+1, n):
        if room[i][1] > room[j][0]:
            continue
        dfs(j,cnt)
    
n = int(input())
room = []
result = []

for i in range(n):
    room.append(list(map(int, input().split())))
    
room.sort(key=lambda x : (x[0],x[1]))
goal = room[-1][0]
for i in range(n):
    dfs(i,0)
print(max(result))
'''
매개변수로 축적된 값을 보낸다고 생각을 못해서 시간이 엄청 걸렸다...
'''