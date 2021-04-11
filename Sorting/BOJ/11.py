#https://www.acmicpc.net/problem/1181
#백준 1181번 단어 정렬(정렬)
n = int(input())#갯수
arr = []
for i in range(n):
    x = input()#입력
    j = [x,len(x)]
    if j not in arr:
        arr.append(j)
u = lambda x : (x[1],x[0])#길이 선순위, 사전순 후순위
arr = sorted(arr,key = u)
for i in arr:
    print(i[0])