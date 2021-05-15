import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = input()
    note = set(input().split())
    m = input()
    print('\n'.join('1' if number in note else '0' for number in input().split()))
'''
굳이 2배열을 빼지 않고 바로 join문을 활용해서 보여주는 방식이 가장 빨랐다.
'''