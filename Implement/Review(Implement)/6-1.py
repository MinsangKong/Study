#https://www.acmicpc.net/problem/4659
#백준 4659번 비밀번호 발음하기(구현)
#import sys
#input = sys.stdin.readline
arr = []
while True:
    n = input()
    if n=='end':
        break
    else:
        arr.append(n)
for i in arr:
    v = 0
    c = 0
    flag = True
    if 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i: 
        if i[0] in 'aeiou':
            v+=1
        else :
            c+=1
        for j in range(1,len(i)):
            if i[j] == i[j-1] and i[j] != 'e' and i[j] != 'o':
                print("<%s> is not acceptable" %i)
                flag = False
                break
            if i[j] in 'aeiou' and i[j-1] in 'aeiou':
                v+=1
                c=0
            elif i[j] not in 'aeiou' and i[j-1] not in 'aeiou':
                c+=1
                v=0
            elif i[j] in 'aeiou':
                v=1
                c=0
            else:
                v=0
                c=1
            if v == 3 or c==3:
                print("<%s> is not acceptable" %i)
                flag = False
                break
        if flag:
            print("<%s> is acceptable" %i)
    else :
        print("<%s> is not acceptable" %i)
'''
for문을 2번 돌려서 시간초과 발생. 생각해보니 굳이 숟자를 하나하나 셀 필요없이 
3개가 연속인지 아닌지만 체크하면 되기 때문에 굳이 for문을 모두 돌릴 필요가 없었다.
너무 비효율적으로 코드를 작성했다. 각각의 check만 처리했으면 더 효율적이었다.
'''