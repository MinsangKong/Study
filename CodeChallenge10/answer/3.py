def lowwer_bound(start,end,queries,target):
    s = start-1
    e = end
    while s+1 < e :
        mid = (s+e) // 2
        mid_value = mid
        for query in queries:
            mid_value += query
            if mid_value < 0 :
                mid_value = 0
            if mid_value >= end :
                mid_value = end - 1
        if mid_value < target :
            s = mid
        else:
            e = mid
    return e
        
def upper_bound(start,end,queries,target):
    s = start - 1
    e = end
    while s+1 < e :
        mid = (s+e) // 2
        mid_value = mid
        for query in queries:
            mid_value += query
            if mid_value < 0 :
                mid_value = 0
            if mid_value >= end :
                mid_value = end -1
        if mid_value <= target :
            s = mid
        else:
            e = mid
    return e

def solution(n, m, x, y, queries):
    directionX = [0,0,-1,1]
    directionY = [-1,1,0,0]
    rows = []
    cols = []
    for query in queries:
        direct, d = query
        if direct > 1 :
            rows.append(d*directionX[direct])
        else:
            cols.append(d*directionY[direct])
    sx = lowwer_bound(0,n,rows,x)
    ex = upper_bound(sx,n,rows,x)
    sy = lowwer_bound(0,m,cols,y)
    ey = upper_bound(sy,m,cols,y)
    print(sx,ex,sy,ey)
    return (ex-sx)*(ey-sy)
print(solution(2,5,0,1,[[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))