#Q2 수식 최대화
#https://programmers.co.kr/learn/courses/30/lessons/67257
from itertools import permutations
import copy

def checker(left,right,op):
    if op=='+':
        return left+right
    elif op=='-':
        return left-right
    else:
        return left*right

def solution(expression):
    answer = 0
    nums = []
    operators = []
    num = ''
    for i in expression:
        if '0' <= i <= '9':
            num+=i
        else:
            if num != '':
                nums.append(int(num))
                num = ''
            operators.append(i)
    if num != '':
        nums.append(int(num))
        
    operation = ['*','+','-']
    testcase = list(map(''.join, permutations(operation)))
    for i in range(len(testcase)):
        case = testcase[i]
        num = copy.deepcopy(nums)
        operator = copy.deepcopy(operators)
        
        for k in range(3):
            oper = case[k]
            j = 0
            while j < len(operator):
                if operator[j] == oper:
                    new = checker(num[j],num[j+1],operator[j])
                    print(new)
                    num[j] = new
                    num.pop(j+1)
                    operator.pop(j)
                    j-=1
                j+=1
        value = abs(num[0])
        answer = max(answer, value)
    return answer
print(solution("50*6-3*2"))