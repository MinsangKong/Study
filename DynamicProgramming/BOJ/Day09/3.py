#https://www.acmicpc.net/problem/2670
#백준 2670번 연속부분 최대곱
#연속한 숫자가 하나 이상이라는 의미는 하나도 포함된다는 뜻. 문제 파악 실수로 시간이 오래걸림
n = int(input())
arr = []
for i in range(n):
    arr.append(float(input()))
if n == 1:
    print(arr[0])
else :
    d = [0]*(n+1)
    d[0] = arr[0]
    d[1] = max(arr[0], arr[1], arr[0]*arr[1])
    for i in range(1, n):
        d[i] = max(arr[i], d[i-1]*arr[i])
    print('%.3f' %round(max(d), 3))
#print('%.3f' %round(max(d), 3))은 맞고 print(round(max(d), 3))은 틀리다
#4번째 자리에서 반올림을 한 값을 3번째자리까지 출력을 해야 이상이 없다.