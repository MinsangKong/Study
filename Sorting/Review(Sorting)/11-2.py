import sys
input = sys.stdin.readline
def solution():
    case = int(input())
    answers = []
    for _ in range(case):
        n = int(input())
        scores = [0]*(n+1)
        for _ in range(n):
            s1, s2 = map(int, input().split())
            scores[s1] = s2
        answer = 1
        min = scores[1]
        for score in scores[2:]:
            if(score<min):
                answer += 1
                min = score
        answers.append(str(answer))
    print('\n'.join(answers))
solution()
'''
이 문제는 기준이 너무 빡빡해서 배열의 수도 최대한 줄이고 답을 출력하는 방식도 최대한
줄여야 속도를 빠르게 할 수 있다.
'''