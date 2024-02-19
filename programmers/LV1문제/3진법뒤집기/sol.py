def solution(n):
    answer = ''
    while n > 0:
        n,r = divmod(n,3) # 몫과 나마지
        answer += str(r)
    return int(answer, 3) # 3진법 기반을 10진법으로 변환

print(solution(45))