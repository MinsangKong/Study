def solution(names, homes, grades):
    answer = []
    data = []
    n = len(names)
    idx = dict()
    for i in range(n):
        data.append([names[i],abs(homes[i][0])**2+abs(homes[i][1])**2,grades[i]])

    data.sort(key = lambda x : (-int(x[2]),-x[1],x[0]))
    for i in range(n):
        idx[data[i][0]] = i+1
    for i in range(n):
        answer.append(idx[names[i]])
    return answer

print(solution(["azad","andy","louis","will","edward"],	[[3,4],[-1,5],[-4,4],[3,4],[-5,0]],[4.19, 3.77, 4.41, 3.65, 3.58]))