def bfs(cases,n,m):
    direction = [(0,-1),(0,1),(-1,0),(1,0)]
    x = y = 0
    for case in cases:
        x += direction[case[0]][0]*case[1]
        y += direction[case[0]][1]*case[1]
    return [x,y]

def solution(n, m, x, y, queries):
    distx,disty = bfs(queries,n,m)
    print(x,y,distx,disty)
    
    if x == 0 and y == m-1 :
        if distx <= 0 and disty >= 0 :
            return min(-distx+1,n)+min(disty+1,m)
        else:
            return 0
    elif x == n-1 and y == 0 :
        if distx >= 0 and disty <= 0 :
            return min(distx+1,n)+min(-disty+1,m)
        else:
            return 0
    elif x == 0 and y == 0 :
        if distx <= 0 and disty <= 0 :
            return min(-distx+1,n)*min(-disty+1,m)
        elif distx <= 0 :
            return min(-distx+1,n)
        elif disty <= 0 :
            return min(-disty+1,m)
        else:
            return 0
    elif x == n-1 and y == m-1 :
        if distx >= 0 and disty >= 0 :
            return min(distx+1,n)*min(disty+1,m)
        elif distx >= 0 :
            return min(distx+1,n)
        elif disty >= 0 :
            return min(disty+1,m)
        else:
            return 0
    elif x == 0 :
        if 0 <= y-disty < m and distx <= 0 :
            return min(-distx+1,n)
        else:
            return 0
    elif y == 0 :
        if 0 <= x-distx < m and disty <= 0 :
            return min(-disty+1,m)
        else:
            return 0
    elif x == n-1 :
        if 0 <= y-disty < m and distx >= 0 :
            return min(distx+1,n)
        else:
            return 0
    elif y == m-1 :
        if 0 <= x-distx < n and disty >= 0 :
            return min(disty+1,m)
        else:
            return 0
    else:
        if 0 <= x-distx < n and 0 <= y-dist < m :
            return 1
        else :
            return 0
        
print(solution(2,2,0,0,[[2,1],[0,1],[1,1],[0,1],[2,1]]))