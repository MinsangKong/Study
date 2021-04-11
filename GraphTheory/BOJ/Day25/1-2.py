#https://www.acmicpc.net/problem/3098
#백준 3098번 소셜 네트워크(그래프 이론, 플로이드)
def f(D):
    return sum([sum(i) for i in D])
total = 0
ans = []
n,m = map(int,input().split())
D = [[0]*(n+1) for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    D[a][b] = 1
    D[b][a] = 1

for i in range(1,n+1):
    D[i][i] = 1


while f(D) < n*n:
    cnt = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if D[i][j] == 1 and D[j][k] == 1 and D[i][k] == 0 and D[k][i] == 0:
                    # print(i,k)
                    D[i][k] = 2
                    D[k][i] = 2
                    cnt+=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if D[i][j] == 2:
                D[i][j] = 1
    ans.append(cnt)
    total+=1
print(total)
for i in ans:
    print(i)
    
'''
남의 코드를 보니 관점을 바꿔서 문제를 풀어도 답은 동일하게 나왔다. 
내가 작성한 것보다 훨씬 깔끔하게 작성했고, sys함수를 적용안해도 속도가 나보다 빨랐다...
아직도 배울 점이 많다.

'''