def solution(n):
    a = sorted(str(n), reverse=True)
    return int(''.join(a))

print(solution(118372))