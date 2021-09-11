def solution(id_list, report, k):
    answer = []
    server = dict()
    counter = dict()
    for i in range(len(id_list)):
        server[id_list[i]] = []
        counter[id_list[i]] = 0
    for i in range(len(report)):
        user, target = report[i].split(' ')
        if target not in server[user]:
            server[user].append(target)
            counter[target]+=1
    for id in id_list:
        cnt = 0
        for target in server[id]:
            if counter[target] >= k:
                cnt+=1
        answer.append(cnt)
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))