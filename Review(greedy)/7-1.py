#https://www.acmicpc.net/problem/13413
#백준 13413번 오셀로 재배치(그리디)
t = int(input())
result = []
for _ in range(t):
    n = int(input())
    oselo = input()
    ans = input()
    check_oselo = []
    check_ans = []
    for i in range(n):
        if oselo[i] != ans[i]:
            check_oselo.append(oselo[i])
            check_ans.append(ans[i])
    cnt = 0
    check_oselo.sort()
    check_ans.sort()
    for i in range(len(check_oselo)):
        if check_oselo[i] == check_ans[i]:
            cnt+=0.5
        else:
            cnt+=1
    print(int(cnt))