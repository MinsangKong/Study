#https://www.acmicpc.net/problem/2872
#백준 2872번 우리집엔 도서관이 있어(그리디)
import sys
#input = sys.stdin.readline
n=int(input())
cnt = 0
book=[]
for i in range(n):
    book.append(int(input()))
check = book[0]
for i in range(1,n) : 
    if book[i] > check :
        if check+1 != book[i] :
            cnt +=1
        check = book[i]
    else :
        cnt +=1
print(cnt)
'''
생각보다 너무 오래 걸렸다. check+1 == book[i]일 때 pass하는 것을 쉽게 안 떠올랐다
'''