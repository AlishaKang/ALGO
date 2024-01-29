# def solution(common):
#     a = common[1] - common[0]
#     b = common[1] // common[0]
#     if common[2] == common[1] + a:
#         result = common[-1] + a
#     else:
#         result = common[-1] * b
#     return result

def solution(common):
    # 등차수열인 경우
    if common[1] - common[0] == common[-1] - common[-2]:
        return common[-1] + (common[1] - common[0])
    # 등비수열인 경우
    else:
        return common[-1] * (common[-1] // common[-2])

print(solution([1, 2, 3, 4]))