def solution(time, plans):
    answer = "호치민"
    total = time
    for i in range(len(plans)):
        name = plans[i][0]
        start = int(plans[i][1][:-2]) if plans[i][1][-2:] == 'AM' else int(plans[i][1][:-2])+12
        end = int(plans[i][2][:-2]) if plans[i][2][-2:] == 'AM' else int(plans[i][2][:-2])+12
        print(start, end)
        if start <= 9.5:
            start = 8.5
        elif start >= 18 :
            start = 0
        else:
            start = 18-start
        if end <= 13 :
            end = 0
        elif end >= 18 :
            end = 5
        else:
            end = end-13
        #print(start+end)
        if total-start-end >= 0 :
            total -= (start+end)
            answer = name
        else:
            break
    return answer