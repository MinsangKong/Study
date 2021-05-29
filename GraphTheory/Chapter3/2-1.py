#Q42 탑승구

g = int(input())
p = int(input())

result = [0]*g
flag = True
cnt = 0

for _ in range(p):
    a = int(input())
    check = False
    if not flag :
        continue
    for i in range(a-1,-1,-1):
        if result[i] == 0:
            result[i] = 1
            check = True
            cnt += 1
            break
    if not check:
        flag = False
        
print(cnt)
        
'''
알고리즘 자체는 맞으나 변수가 많아질수록(75%에서) 시간초과 발생
'''