from collections import defaultdict

def solution(weights):
    cnt = 0
    pos = [(2, 3), (2, 4), (3, 4), (4, 3), (4, 2), (3, 2)]
    dic = defaultdict(int)

    for weight in weights:
        dic[weight] += 1

    for mw in dic:
        if dic[mw] > 1:
            cnt += dic[mw] * (dic[mw] - 1) // 2
        for mpos, fpos in pos:
            expected_fw = mw * mpos / fpos
            if expected_fw in dic:
                cnt += dic[mw] * dic[expected_fw]
        dic[mw] = 0

    return cnt
