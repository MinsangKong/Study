#https://www.acmicpc.net/problem/2941
#백준 2941번 구현
#import sys
#input = sys.stdin.readline
alp = input()
cro_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt =0
for i in cro_alp:
    if i in alp :
        cnt+=alp.count(i)
        alp = alp.replace(i,"0")
for i in range(cnt):
    alp = alp.replace("0","")
result = len(alp)+cnt
print(result)
'''
 다른 사람들의 코드를 보니까 굳이 replace 한 다음에 횟수를 안 세어도 괜찮았다.
 print(len(alp) - sum(alp.count(c) for c in cro_alp)) 이런 식으로 바로 구해서 
 계산했어도 문제가 없었다. 비효율적으로 코드를 작성했다.
'''