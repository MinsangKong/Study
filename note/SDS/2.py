# 전자 숫자판
# 21.06.19

import sys
from collections import deque
import copy

rd = sys.stdin.readline
INF = int(1e9)


def main():
    t = int(rd())
    case = 1

    while case <= t:
        a, b, l = rd().split()
        l = int(l)
        filter1 = rd().rstrip()
        filter2 = "".join(reversed(filter1))

        num = ""
        for i in range(6 - len(a)):
            num += "0"
        num += a
        a = num

        num = ""
        for i in range(6 - len(b)):
            num += "0"
        num += b
        b = num

        A, B = [], []

        for i in range(6):
            A.append(int(a[i]))
            B.append(int(b[i]))

        def calc(start, target, f):
            idx = 0
            if f[0] == "0":
                idx += 1
                while idx < l:
                    if f[idx] != "0":
                        break
                    idx += 1
                if idx == l:
                    return -1

            cnt = 0
            stop = False
            while target[start + idx] != B[start + idx]:
                for i in range(l):
                    if f[i] == "+":
                        if target[start + i] == 9:
                            stop = True
                            break
                        target[start + i] += 1
                    elif f[i] == "-":
                        if target[start + i] == 0:
                            stop = True
                            break
                        target[start + i] -= 1
                if stop: return cnt

                cnt += 1
            return cnt


        def solution(head, end, arr, cnt):
            if head > end:
                for i in range(6):
                    if arr[i] != B[i]:
                        return INF
                return cnt
            else:
                arr1 = copy.deepcopy(arr)
                arr2 = copy.deepcopy(arr)
                arr3 = copy.deepcopy(arr)

                cnt2 = calc(head, arr2, filter1)
                cnt3 = calc(head, arr3, filter2)

                ans1 = solution(head + 1, end, arr1, cnt)
                ans2, ans3 = INF, INF

                if cnt2 > -1:
                    ans2 = solution(head + 1, end, arr2, cnt + cnt2)
                if cnt3 > -1:
                    ans3 = solution(head + 1, end, arr3, cnt + cnt3)

                return min(ans1, ans2, ans3)


        result = solution(0, 6 - l, A, 0)

        if result == INF:
            result = -1

        print(f"#{case} {result}")

        case += 1


main()