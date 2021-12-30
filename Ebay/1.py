def change(key):
    if len(key) == 8:
        date = key[:2]
        h = int(key[3:5]) 
        m = int(key[6:])
        return [date,h,m]
    else:
        date1 = key[:2]
        h1 = int(key[3:5]) 
        m1 = int(key[6:8])
        date2 = key[9:11]
        h2 = int(key[12:14]) 
        m2 = int(key[15:])
        return [[date1,h1,m1],[date2,h2,m2]]
def solution(schedule):
    answer = 1024
    day = {'MO':0, 'TU':1, 'WE':2, 'TH':3, 'FR':4 }
    for a in range(4):
        week = [dict() for _ in range(5)]
        if len(schedule[0][a]) == 8 :
            c1 = change(schedule[0][a])
            date, h, m = c1
            time = h*60+m
            week[day[date]][time] = 1
            week[] 

        for b in range(4):
            for c in range(4):
                for d in range(4):
                    for e in range(4)
    return answer