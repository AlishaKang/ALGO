def solution(num):
    cnt = 0
    while num != 1:
        if num  % 2 == 0 and cnt < 500:
            num//=2
            cnt += 1
        elif num % 2 == 1 and num != 1 and cnt < 500:
            num = num*3+1
            cnt += 1
        elif cnt >= 500:
            return -1
    return cnt
        
print(solution(6))