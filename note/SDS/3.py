import sys
#input = sys.stdin.readline
sys.setrecursionlimit(100000)
result = int(1e9)
flag = False
def dfs(cnt,position, graph, direction,visited,check,idx):
    global result
    global flag
    if flag:
        return
    if position[0][1] == 4:
        result = min(result,cnt)
        flag = True
        return
    for i in range(len(position)):
        x, y = position[i][0], position[i][1]
        direct = direction[i]
        if direct == 'E' :
            if y+1 < 5 and [x,y,x,y+1] not in visited[i]:
                if graph[x][y+1] == -1:
                    graph[x][y+1] = i
                    graph[x][y-1] = -1
                    position[i][1] += 1
                    visited[i].append([x,y,x,y+1])
                    if idx == i and check[i] == 0: #0이면 정방향 1이면 역방향
                        dfs(cnt,position, graph, direction,visited,check,i)
                    else:
                        check[i] = 0
                        dfs(cnt+1,position, graph, direction,visited,check,i)
                    graph[x][y+1] = -1
                    graph[x][y-1] = i
                    position[i][1] -= 1
                    visited[i].pop()
            if 0 <= y-2 and [x,y-2,x,y-1] not in visited[i]:
                if graph[x][y-2] == -1:
                    graph[x][y-2] = i
                    graph[x][y] = -1
                    position[i][1] -=1
                    visited[i].append([x,y-2,x,y-1])
                    if idx == i and check[i] == 1: #0이면 정방향 1이면 역방향
                        dfs(cnt,position, graph, direction,visited,check,i)
                    else:
                        check[i] = 1
                        dfs(cnt+1,position, graph, direction,visited,check,i)
                    visited[i].pop()
                    graph[x][y-2] = -1
                    graph[x][y] = i
                    position[i][1] +=1
            
        elif direct == 'W' :
            if y+2 < 5 and [x,y+1,x,y+2] not in visited[i]:
                if graph[x][y+2] == -1:
                    graph[x][y+2] = i
                    graph[x][y] = -1
                    position[i][1] += 1
                    visited[i].append([x,y+1,x,y+2])
                    if idx == i and check[i] == 1: #0이면 정방향 1이면 역방향
                        dfs(cnt,position, graph, direction,visited,check,i)
                    else:
                        check[i] = 1
                        dfs(cnt+1,position, graph, direction,visited,check,i)
                    graph[x][y+2] = -1
                    graph[x][y] = i
                    position[i][1] -= 1
                    visited[i].pop()
            if 0 <= y-1 and [x,y-1,x,y] not in visited[i]:
                if graph[x][y-1] == -1:
                    graph[x][y-1] = i
                    graph[x][y+1] = -1
                    position[i][1] -= 1
                    visited[i].append([x,y-1,x,y])
                    if idx == i and check[i] == 0: #0이면 정방향 1이면 역방향
                        dfs(cnt,position, graph, direction,visited,check,i)
                    else:
                        check[i] = 0
                        dfs(cnt+1,position, graph, direction,visited,check,i)
                    graph[x][y-1] = -1
                    graph[x][y+1] = i
                    position[i][1] += 1
                    visited[i].pop()
        elif direct == 'N' :
            if 0 <= x-1 and [x-1,y,x,y] not in visited[i]:
                if graph[x-1][y] == -1:
                    graph[x-1][y] = i
                    graph[x+1][y] = -1
                    position[i][0] -= 1
                    visited[i].append([x-1,y,x,y])
                    if idx == i and check[i] == 0: #0이면 정방향 1이면 역방향
                        dfs(cnt,position, graph, direction,visited,check,i)
                    else:
                        check[i] = 0
                        dfs(cnt+1,position, graph, direction,visited,check,i)
                    graph[x-1][y] = -1
                    graph[x+1][y] = i
                    position[i][0] += 1
                    visited[i].pop()
            if x+2 < 5 and [x+1,y,x+2,y] not in visited[i]:
                if graph[x+2][y] == -1:
                    graph[x+2][y] = i
                    graph[x][y] = -1
                    position[i][0] += 1
                    visited[i].append([x+1,y,x+2,y])
                    if idx == i and check[i] == 1: #0이면 정방향 1이면 역방향
                        dfs(cnt,position, graph, direction,visited,check,i)
                    else:
                        check[i] = 1
                        dfs(cnt+1,position, graph, direction,visited,check,i)
                    graph[x+2][y] = -1
                    graph[x][y] = i
                    position[i][0] -= 1
                    visited[i].pop()
        elif direct == 'S':
            if 0 <= x-2 and [x-1,y,x-2,y] not in visited[i]:
                if graph[x-2][y] == -1:
                    graph[x-2][y] = i
                    graph[x][y] = -1
                    position[i][0] -= 1
                    visited[i].append([x-1,y,x-2,y])
                    if idx == i and check[i] == 1: #0이면 정방향 1이면 역방향
                        dfs(cnt,position, graph, direction,visited,check,i)
                    else:
                        check[i] = 1
                        dfs(cnt+1,position, graph, direction,visited,check,i)
                    graph[x-2][y] = -1
                    graph[x][y] = i
                    position[i][0] += 1
                    visited[i].pop()
            if x+1 < 5 and [x,y,x+1,y] not in visited[i]:
                if graph[x+1][y] == -1:
                    graph[x+1][y] = i
                    graph[x-1][y] = -1
                    position[i][0] += 1
                    visited[i].append([x,y,x+1,y])
                    if idx == i and check[i] == 0: #0이면 정방향 1이면 역방향
                        dfs(cnt,position, graph, direction,visited,check,i)
                    else:
                        check[i] = 0
                        dfs(cnt+1,position, graph, direction,visited,check,i)
                    graph[x+1][y] = -1
                    graph[x-1][y] = i
                    position[i][0] -= 1
                    visited[i].pop()
                    
def main():
    # 이곳에 소스코드를 작성하세요.
    # Python3 만 지원됩니다.
    # pass는 삭제해도 됩니다.
    idx = 1
    t = int(input())
    for _ in range(t):
        n = int(input())
        graph = [[-1]*5 for _ in range(5)]
        global result
        result = int(1e9)
        global flag
        flag = False
        direction = []
        position = []
        visited = [[] for _ in range(n)]
        check = [[-1] for _ in range(n)] #같은 방향일 경우 cnt를 안 늘려주기 위해 check 배열을 사용
        for i in range(n):
            a,b,direct = input().split()
            direction.append(direct)
            position.append([int(a)-1,int(b)-1])
            if direct == 'E':
                graph[int(a)-1][int(b)-1] = i
                graph[int(a)-1][int(b)-2] = i
                visited[i].append([int(a)-1,int(b)-2,int(a)-1,int(b)-1])
            elif direct == 'W':
                graph[int(a)-1][int(b)-1] = i
                graph[int(a)-1][int(b)] = i
                visited[i].append([int(a)-1,int(b)-1,int(a)-1,int(b)])
            elif direct == 'N':
                graph[int(a)-1][int(b)-1] = i
                graph[int(a)][int(b)-1] = i
                visited[i].append([int(a)-1,int(b)-1,int(a),int(b)-1])
            else:
                graph[int(a)-1][int(b)-1] = i
                graph[int(a)-2][int(b)-1] = i
                visited[i].append([int(a)-2,int(b)-1,int(a)-1,int(b)-1])
        dfs(0,position, graph, direction,visited,check,n+1)
        if result < int(1e9):
            print("#%d %d" % (idx, result//2))
        else:
            print("#%d %d" % (idx, -1))
        idx+=1
main()