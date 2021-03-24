#https://www.acmicpc.net/problem/2504
#백준 2504번 괄호의 값(구현, 스택활용)
#import sys
#input = sys.stdin.readline
s = input().rstrip()
stack = []
result = 0

for i in s:
    if i == ')':
        last = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '(':
                if last == 0:
                    stack.append(2)
                else:
                    stack.append(2 * last)
                break
            elif top == '[':
                print(0)
                exit(0)
            else:
                last+=int(top)
 
    elif i == ']':
        last = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '[':
                if last == 0:
                    stack.append(3)
                else:
                    stack.append(3 * last)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                last += int(top)
 
    else:
        stack.append(i)

for i in stack:
    if i == '(' or i == '[':
        print(0)
        exit(0)
print(sum(stack))
'''
엄청 해매다가 stack을 활용해서 풀었다. 아직도 stack을 조절해서 사용하는 것이 미숙하다.
가장 빠르게 푼 사람의 함수를 보니까 eval 함수로 빠르게 풀었다.
eval 함수는 매개변수로 받은 expression(python에 인지 가능한 표현식)을 문자열로
받아서 실행하는 함수이다. 문자열을 사용해서 계산을 편하게 할 수 있지만
eval() 명령은 코드의 가독성을 떨어뜨리고 디버깅을 어렵게 만들수 있기 때문에
사용을 추천하지 않는다.(global 변수처럼 최대한 덜 사용)
'''