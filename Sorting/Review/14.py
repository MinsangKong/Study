#https://www.acmicpc.net/problem/5052
#백준 5052번 전화번호 목록(정렬)
#import sys
#input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    book = [input().rstrip() for _ in range(n)]
    book.sort()
    flag = True
    for i in range(n-1):
        if book[i] in book[i+1][:len(book[i])]:
            flag = False
            break      
    if flag:          
        print("YES")
    else:
        print("NO")
'''
개 거지 같은 문제. 알고리즘은 아무리 생각해도 맞다고 생각해서 구글링해서 찾아보니까
어느 순간부터 rstrip()을 안하면 정답처리를 안했다. 입력에 자동적으로 공백이 있었던게
함정인데 다음부터는 하나 입력 받으면 rstrip()을 하는 버릇을 드려야겠다.
'''