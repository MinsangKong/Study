INF = int(1e9)
t=int(input())

while t :
    n=int(input())
    a=[list(map(int, input().split())) for i in range(n+2)]
    d=[[INF] * (n+2) for i in range(n+2)]
    
    for i in range(n+2):
        for j in range(n+2):
            if i == j :
                continue
            di=abs(a[i][0]-a[j][0]) + abs(a[i][1]-a[j][1])
    
            if di <= 1000:
                d[i][j] = 1

    for k in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
    
    if 0 <= d[0][n+1] < INF:
        print('happy')
    else:
        print('sad')
  
    t -= 1