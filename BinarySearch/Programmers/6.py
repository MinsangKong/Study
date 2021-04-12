#https://programmers.co.kr/learn/courses/30/lessons/42883
#levle 2 큰 수 만들기(그리디)
def solution(number, k):
    answer = ''
    idx = 0
    answer_len = len(number)-k
    max = '0'
    #max 함수를 쓰는 경우 무조건 10번에서 에러 발생
    for i in range(answer_len): #남아 있는 숫자가 딱 맞을 경우
        if len(number) == answer_len-i :
            answer += number      
            break;
        max = '0' #max 함수를 못 쓰기 때문에 자리 수를 바꿀 때마다 계속 max를 초기화
        for e in range(0, len(number)-(answer_len-i)+1):
            if number[e] == '9':
                max = '9'
                idx = e
                break #testcase 10에서 9가 계속 반복되기 때문에 일일히 비교하면 runtime 에러 발생하므로 9를 만나면 바로 break하고 숫자를 추가 
            else:
                if ord(number[e]) > ord(max): #문자열 숫자를 비교하기 위해 아스키코드로 비교
                    max = number[e]
                    idx = e
        answer += str(max)
        number = number[idx+1:]

    return answer