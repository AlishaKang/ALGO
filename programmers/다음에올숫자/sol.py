def solution(common):
    a = common[1] - common[0]
    b = common[1] // common[0]
    if common[2] == common[1] + a:
        result = common[-1] + a
    else:
        result = common[-1] * b
    return result

print(solution([1, 2, 3, 4]))