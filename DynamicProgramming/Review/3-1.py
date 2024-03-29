#https://www.acmicpc.net/problem/17626
#백준 17626번 Four Squares(DP)
#import sys
#input = sys.stdin.readline

def four_square(n):
    c = 1
    check = 0
    temp = [n]
    while True:
        if c == 3:
            c += 1
            break
        temp_temp = temp
        temp = []
        for i in temp_temp:
            for j in one:
                if j < i:
                    temp.append(i - j)
        for i in temp:
            if i in one:
                check = 1
                break
        c += 1
    return c

num = int(input())
one = {x ** 2: 0 for x in range(223, 0, -1)}
if num in one:
    print(1)
else:
    print(four_square(num))