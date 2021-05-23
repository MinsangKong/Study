#Q38 정확한 순위

n, m = map(int, input().split())

graph = [[0]*n for _ in range(n)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = -1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][j] == 0:
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    
result = 0
for i in range(n):
    if graph[i].count(0) == 1:
        result+=1
print(result)