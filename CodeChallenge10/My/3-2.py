def lowwer_bound(start,end,queries,direction,target):
    s = start
    e = end #원래 이분탐색에서는 e+1로 해서 아웃오브 바운드를 고려해야 하지만
            #여기서는 결국 최대값은 end-1이기 때문에 e = end-1+1이 된다
    while s < e :
        mid = (s+e) // 2
        mid_value = mid
        for query in queries:
            mid_value += direction[query[0]]*query[1]
            if mid_value < 0 :
                mid_value = 0
            if mid_value >= end :
                mid_value = end -1
        if mid_value < target :
            s = mid + 1
        else:
            e = mid
    return e
        
def upper_bound(start,end,queries,direction,target):
    s = start
    e = end
    while s < e :
        mid = (s+e) // 2
        mid_value = mid
        for query in queries:
            mid_value += direction[query[0]]*query[1]
            if mid_value < 0 :
                mid_value = 0
            if mid_value >= end :
                mid_value = end -1
        if mid_value <= target :
            s = mid + 1
        else:
            e = mid
    return e

def solution(n, m, x, y, queries):
    directionX = [0,0,-1,1]
    directionY = [-1,1,0,0]
    sx = lowwer_bound(0,n,queries,directionX,x)
    ex = upper_bound(sx,n,queries,directionX,x)
    sy = lowwer_bound(0,m,queries,directionY,y)
    ey = upper_bound(sy,m,queries,directionY,y)
    print(sx,ex,sy,ey)
    return (ex-sx)*(ey-sy)
print(solution(2,5,0,1,[[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))
'''
결국 범위를 구해보면 x와 y의 값이 경계에 위치한다면 이를 만족하는 값은 
연속된 공간에 존재한다. 따라서 가로와 세로로 나눠서 이를 만족하는 구간을
파라매트릭 서치로 구하면 원하는 결과값을 구할 수 있다.
'''