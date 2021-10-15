#https://www.acmicpc.net/problem/2504
#백준 2504번 괄호의 값(스택, 문자열)
import sys
#input = sys.stdin.readline
s = input().rstrip()
stack = []
result = 0

for i in range(len(s)):
    if s[i] == ')':
        if i == 0:
            print(0)
            sys.exit(0)
        last = 0
        while stack:
            top = stack.pop()
            if top == '(':
                if last == 0:
                    stack.append(2)
                else:
                    stack.append(2 * last)
                break
            elif top == '[':
                print(0)
                sys.exit(0)
            else:
                last+=int(top)

    elif s[i] == ']':
        if i == 0:
            print(0)
            sys.exit(0)        
        last = 0
        while stack:
            top = stack.pop()
            if top == '[':
                if last == 0:
                    stack.append(3)
                else:
                    stack.append(3 * last)
                break
            elif top == '(':
                print(0)
                sys.exit(0)
            else:
                last += int(top)

    else:
        stack.append(s[i])

for i in stack:
    if i == '(' or i == '[':
        print(0)
        sys.exit(0)

print(sum(stack))