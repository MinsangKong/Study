import sys
N = int(input())

dic = {}
for i in range(N):
    dic[i+1] = int(sys.stdin.readline())
    

def dfs(graph,start,visited=[]):
    if start not in visited:
        visited.append(start)
    
    if(dic[start] in visited):
        if(dic[start] == visited[0]):
            return 1
        else:
            return 0
    else:
        visited.append(dic[start])
        return dfs(graph,dic[start],visited)


A = []
for i in range(1,N+1):
    visited = []
    if(dfs(dic,i,visited)):
        A.append(i)
        
print(len(A))
for i in A:
    print(i)
'''
딕셔너리를 활용한 사람이 근소하게 실행속도가 더 빨랐다.
'''