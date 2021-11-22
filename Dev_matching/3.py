from collections import deque
from statistics import mean, mode

def get_prime_pulse(pulse):
    max_len = len(pulse)
    freq = 0
    while freq < max_len:
        freq += 1
        # Skip cannot divisible
        if max_len % freq != 0:
            continue
        diff_detect = False
        for i in range(freq):
            curs = [ pulse[x+i] for x in [ p*freq for p in range(max_len//freq)]]
            if min(curs) != max(curs):
                diff_detect = True
                break
        if diff_detect == False:
            break
    return pulse[:freq]

def solution(pulse1, pulse2):
    pulse1 = get_prime_pulse(pulse1)
    pulse2 = get_prime_pulse(pulse2)

    wave1, wave2 = [], []
    wave1 += pulse1
    wave2 += pulse2
    while len(wave1) != len(wave2):
        if len(wave1) < len(wave2):
            wave1 += pulse1
        else:
            wave2 += pulse2

    min_adjust = min(len(pulse1), len(pulse2))
    wave2 = deque(wave2)
    answer = 100000**2 * len(wave1)
    for kinds in range(min_adjust):
        combined = []
        for i in range(len(wave1)):
            combined.append(wave1[i] + wave2[i])
        wave2.rotate(1)

        combined = get_prime_pulse(combined)
        min_stat, max_stat = min(combined), max(combined)
        variances = [answer]
        base = int(mean(combined))
        variances.append(sum([ (c - base-1) ** 2 for c in combined ]))
        variances.append(sum([ (c - base) ** 2 for c in combined ]))
        variances.append(sum([ (c - base+1) ** 2 for c in combined ]))
        base = int(mode(combined))
        variances.append(sum([ (c - base-1) ** 2 for c in combined ]))
        variances.append(sum([ (c - base) ** 2 for c in combined ]))
        variances.append(sum([ (c - base+1) ** 2 for c in combined ]))
        answer = min(variances)
    return answer