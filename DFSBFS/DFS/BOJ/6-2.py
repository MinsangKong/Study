import collections


def main():
    N, S = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]

    first, second = [0], [0]
    for num in nums[:N // 2]:
        first.extend([num + x for x in first])
    for num in nums[N // 2:]:
        second.extend([num + x for x in second])
    second_counter = collections.Counter(second)

    answer = sum(second_counter[S - f] for f in first)
    if S == 0:
        answer -= 1
    print(answer)


if __name__ == '__main__':
    main()