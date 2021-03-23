#https://www.acmicpc.net/problem/2204
#백준 2204번 도비의 난독증 테스트(구현)
#import sys
#input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    for i in range(n):
        word = input()
        arr.append((word.lower(), word))
    arr.sort()
    print(arr[0][1])
'''
출력 형식이 잘못 되었습니다 오류가 발생한 경우에는 input=sys.stdin.readline을 하지말고
아예 input() 위치에 sys.stdin.readline().rstrip()을 하면 오류가 발생하지 않는다.
다른 사람의 코드를 보니까 속도면에서는 의외로 dictionary가 근소하게 빠르다.
'''