def solution(n, left, right):
    answer = []
    sx,sy = divmod(left,n)
    ex,ey = divmod(right,n)

    if sx == ex  :
        for i in range(sy,ey+1):
            answer.append(max(ex,i)+1)
    else:
        for i in range(sy,n):
            answer.append(max(sx+1,i+1))
        for i in range(sx+1,ex):
            for j in range(n):
                answer.append(max(i+1,j+1))
        for i in range(ey+1):
            answer.append(max(ex+1,i+1))
    #print(answer)
    return answer

print(solution(3,3,4))