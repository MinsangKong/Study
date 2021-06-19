import sys
input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    num = input().rstrip()
    check = 0
    start = int(num)
    temp = list(num)
    flag = False
    result = [start]
    if start == 1:
        flag = True
    while True:
        if check == 1:
            flag = True
            break
        else:
            check = 0 
        for i in temp:
            check +=int(i)**2
        if check not in result:
            result.append(check)
            temp = list(map(str, str(check)))
        else:
            break

    if flag:
        print("%d is Happy Number." %start)
    else:
        print("%d is Unhappy Number." %start)