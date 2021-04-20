N = int(input())
sells = dict()

for _ in range(N) :
    book = input()
    if book in sells :
        sells[book] += 1
    else :
        sells[book] = 1

sells = sorted(sells.items())
print(sorted(sells, key=lambda x: x[1], reverse=True)[0][0])
"""
역시 가장 빠르게 푸는 방법은 dictionary를 활용한 방법이었다.
"""