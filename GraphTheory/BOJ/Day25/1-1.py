#https://www.acmicpc.net/problem/3098
#백준 3098번 소셜 네트워크(그래프 이론, 플로이드)
#sys import
#input = sys.stdin.readline
n, m = map(int, input().split())
friend = [[0]*(n+1) for _ in range(n+1)] #친구 수 체크
change = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    friend[a][b]=1
    friend[b][a]=1
result = []
day = 0    
while True:
    cnt = 0
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i == j:
                    continue
                if friend[i][j] == 0 and friend[i][k] == 1 and friend[k][j] == 1:
                    if change[i][k] <=day and change[k][j] <=day:
                        friend[i][j] = 1
                        friend[j][i] = 1
                        change[i][j] = day+1
                        change[j][i] = day+1
                        cnt+=1
    if cnt==0:
        break
    day+=1
    result.append(cnt)
    
print(day)
for i in result:
    print(i)
        
'''
배열을 굳이 2개 안만들어도 자체적으로 값을 변화시키는 걸로 해결 가능한 문제였다.
시간 효율 면에서는 비효율적으로 문제를 해결했다.
'''