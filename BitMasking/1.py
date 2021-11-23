#https://www.acmicpc.net/problem/1052
#백준 1052번 물병 (비트마스킹)
#import sys
#input = sys.stdin.readline

n, k = map(int, input().split())
result = 0
count = bin(n).count('1')

while count > k :
    num = n &(-n)
    result += num
    n += num
    count = bin(n).count('1')

print(result)
'''
bit 값의 가장 오른쪽 위치 반환 : n&(-n)
n = 001  -n =  111   --->    n&-n = 001
n = 010  -n =  110   --->    n&-n = 010
n = 100  -n = 100   --->    n&-n = 100
'''