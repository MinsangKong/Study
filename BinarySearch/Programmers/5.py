#https://programmers.co.kr/learn/courses/30/lessons/42860
#level 2 조이스틱(그리디)
def solution(name):
    joy = []
    answer = 0
    #배정
    for i in range(len(name)):
        if name[i]=='A':
            continue
        else:
            joy.append(i)
        temp = ord(name[i])-ord('A')
        if temp>13:
            answer += 26-temp
        else:
            answer += temp
    #이제 index 기반으로 다음 위치 그리디하게 찾기
    current = 0
    for i in range(len(joy)):
        move_list = [abs(x-current) if abs(x-current)<=len(name)/2 else len(name)-abs(x-current) for x in joy]
        answer += min(move_list)
        current = joy.pop(move_list.index(min(move_list)))
    return answer