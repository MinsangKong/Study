def solution(inputString):
    length = len(inputString)
    answer = 0
    check = []
    points =[')','}',']','>']
    starts =['(','}','[','<']
    flag = True
    for i in range(length):
        if i == 0 :
            if inputString[i] in points:
                break
            else:
                check.append(inputString[i])
        elif inputString[i] == points[0]:
            flag = False
            while check:
                point = check.pop()
                if point == '(':
                    answer+=1
                    flag = True
                    break
                elif point == '{':
                    return -i
                elif point == '[':
                    return -i
                elif point == '<':
                    return -i
            if not flag:
                answer = -i
                break
        elif inputString[i] == points[1]:
            flag = False
            while check:
                point = check.pop()
                if point == '{':
                    answer+=1
                    flag = True
                    break
                elif point == '(':
                    return -i
                elif point == '[':
                    return -i
                elif point == '<':
                    return -i
                
            if not flag:
                answer = -i
                break
        elif inputString[i] == points[2]:
            flag = False
            while check:
                point = check.pop()
                if point == '[':
                    answer+=1
                    flag = True
                    break
                elif point == '(':
                    return -i
                elif point == '{':
                    return -i
                elif point == '<':
                    return -i
            if not flag:
                answer = -i
                break
        elif inputString[i] == points[3]:
            flag = False
            while check:
                point = check.pop()
                if point == '<':
                    answer+=1
                    flag = True
                    break
                elif point == '{':
                    return -i
                elif point == '[':
                    return -i
                elif point == '(':
                    return -i
            if not flag:
                answer = -i
                break
        else:
            check.append(inputString[i])
    if check:
        for i in starts:
            if i in check:
                return -length+1
    return answer
print(solution("line [({<plus>})"))