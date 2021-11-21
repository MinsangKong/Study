def solution(rows, columns, connections, queries):
    answer = []
    data = connections[:]
    for i in range(len(queries)):
        x1,y1,x2,y2 = queries[i]
        count = 0
        temp = []
        limit = dict()
        for i in range(min(x1,x2),max(x1,x2)+1):
            for j in range(min(y1,y2),max(y1,y2)+1):
                limit[i*columns+j] = 1
        print(limit)
        for r1,c1,r2,c2 in data:
            a = r1*columns+c1
            b = r2*columns+c2
            print(a,b)
            if a in limit and b in limit :
                temp.append([r1,c1,r2,c2])
            elif a in limit or b in limit :
                count += 1
            else:
                temp.append([r1,c1,r2,c2])
        answer.append(count)
        data = temp

    return answer

print(solution(2,2,[[1,1,1,2],[2,2,1,2],[2,1,1,1],[2,2,2,1]],[[1,1,2,2],[1,1,2,1],[2,1,2,2]]))