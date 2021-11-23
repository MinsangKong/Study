#https://www.acmicpc.net/problem/11723
#백준 11723번 집합 (비트마스킹)
#import sys
#input = sys.stdin.readline
INF = (1 << 20)-1

n = int(input())
bit = 0
result = ""

for _ in range(n):
    data = input().split()
    if data[0][0] == 'a':
        if data[0][1] == 'd':
            bit |= 1 << (int(data[1])-1)
        else:
            bit = INF
    elif data[0][0] == 'r':
        bit &= ~(1 << (int(data[1])-1))
    elif data[0][0] == 'c':
        if bit & 1 << (int(data[1])-1):
            result += '1\n'
        else:
            result += '0\n'
    elif data[0][0] == 't':
        bit ^= 1 << (int(data[1])-1)
    else:
        bit = 0
        
print(result)
#pypy3로 실행되려면 sys.stdout.write('1\n')을 써야한다