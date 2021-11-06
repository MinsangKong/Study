def solution(log):
    total = 0
    for i in range(0,len(log),2):
        start = int(log[i][:2])*60+int(log[i][3:])
        end = int(log[i+1][:2])*60+int(log[i+1][3:])
        studyTime = end-start

        if studyTime < 5:
            continue
        elif end-start > 105:
            studyTime = 105
        total += studyTime

    hour, minute = divmod(total,60)
    hour = '0'+str(hour) if hour < 10 else str(hour)
    minute = '0'+str(minute) if minute < 10 else str(minute)
    return hour+":"+minute