import math

def solution(fees, records):
    checker = dict()
    costs = dict()
    answer = []

    for record in records:
        time, id, state = record.split(' ')
        if state == 'OUT':
            sh = int(checker[int(id)][:2])
            sm = int(checker[int(id)][3:])
            eh = int(time[:2])
            em = int(time[3:])
            costs[int(id)] += (eh-sh)*60 + (em-sm)
            del checker[int(id)]
        else:
            checker[int(id)] = time
            if int(id) not in costs:
                costs[int(id)] = 0

    for id in sorted(costs):
        if id in checker:
            sh = int(checker[id][:2])
            sm = int(checker[id][3:])
            costs[id] += (23-sh)*60 + (59-sm)
        money = fees[1]

        if costs[id] > fees[0]:
            costs[id]-=fees[0]
            money += math.ceil(costs[id]/fees[2])*fees[3]
        answer.append(money)

    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))