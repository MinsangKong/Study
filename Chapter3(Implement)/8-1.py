#Q14 외벽 점검
def solution(n, weak, dist):
    from itertools import permutations
    answer = len(dist) + 1 # 점검이 불가능한 경우 가정
    weak_length = len(weak)

    #1. 길이를 두배로 늘리면 방향을 고려할 필요가 없음
    for i in range(weak_length):
        weak.append(weak[i] + n)

    dist_combin = list(map(list,permutations(dist,len(dist)))) #2. dist의 모든 경우의 수를 구한다.

    for i in range(weak_length):
        start = [weak[j] for j in range(i, i+weak_length)] #시작점을 하나씩 바꾸면서, weak의 길이만큼 잘라서 사용한다.
        for dist_p in dist_combin:
            result = 1 # dist 친구 활용 개수
            dist_distance = 0 #거리
            check_len = start[0] + dist_p[0] # dist의 친구가 확인할 수 있는 최대 거리

            for k in range(weak_length):
                if start[k] > check_len: #확인 가능한 최대 거리를 넘었을 경우
                    result += 1 # 활용되는 dist의 친구 수 추가
                    # 더이상 투입 인원이 없을 경우
                    if result > len(dist_p):
                        break
                    dist_distance += 1 #다음친구를 투입
                    check_len = start[k] + dist_p[dist_distance] #친구가 확인할 수 있는 거리 업데이트

            answer = min(answer,result) #작은 값을 선택한다.

    if answer > len(dist): #만약 weak를 다 체크하지 못하면 -1 리턴
         return -1
    return answer
'''
맨 처음으로 이해한 코드에서는 for문을 반복할 때마다 순열을 생성했기 때문에 
시간초과가 발생했다. 근데 이 문제는 문제를 푸는 방식이 여러 가지인데
이해하기가 좀 많이 어려웠다...
'''