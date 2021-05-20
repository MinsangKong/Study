import sys
#input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[0]*n for _ in range(n)]

for i in range(k):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j :
                continue
            if graph[i][k] != 0 and graph[k][j] != 0 :
                if graph[i][j] == 0 or graph[i][j] > graph[i][k]+graph[k][j]:
                    graph[i][j] = graph[i][k]+graph[k][j]

flag = True
for i in range(n):
    for j in range(n):
        if (graph[i][j] == 0 and i != j) or graph[i][j] > 6:
            flag = False
            break
if flag:
    print("Small World!")
else:
    print("Big World!")

    
'''
계속 틀린 이유는 6단계가 넘어가는 것을 체크 하지 않았기 때문에 시간이 오래걸렸다.
'''