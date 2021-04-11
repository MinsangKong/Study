#https://www.acmicpc.net/problem/1475
#백준 1475번 방 번호(구현)
#import sys
#input = sys.stdin.readline
a = input()
a = a.replace('6','9')
res = 0
for i in range(10):
    cnt = a.count(str(i))
    if i == 9:
        cnt = int(cnt/2)+cnt%2
    if res < cnt:
        res = cnt
print(res)
'''
이 문제도 점화식으로 간단하게 풀 수 있었다. 굳이 조건을 안 나눠도 
cnt = int(cnt/2)+cnt%2로 6이나 9의 숫자의 개수가 홀수인지 짝수인지로 답을 쉽게 알 수 있다.
'''