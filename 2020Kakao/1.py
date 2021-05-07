#Q1 키패드 누르기
#https://programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = ''
    left_place = 4
    left_idx = 1
    right_place = 4
    right_idx = 3
    
    for i in numbers:
        place, idx = i//3, i%3
        if i == 0 :
            place , idx = 3, 2
        if idx == 1:
            left_place, left_idx = place+1, idx
            answer+= 'L'
        elif idx == 0 :
            right_place, right_idx = place, 3
            answer += 'R'
        else:
            if hand == "left":
                if abs(place+1-left_place)+abs(2-left_idx) <= abs(right_place-place-1)+abs(right_idx-2):
                    left_place, left_idx = place + 1, idx
                    answer+= 'L'
                else:
                    right_place, right_idx = place + 1, idx
                    answer+= 'R'
            else:
                if abs(place+1-left_place)+abs(2-left_idx) < abs(right_place-place-1)+abs(right_idx-2):
                    left_place, left_idx = place + 1, idx
                    answer+= 'L'
                else:
                    right_place, right_idx = place + 1, idx
                    answer+= 'R'
    return answer