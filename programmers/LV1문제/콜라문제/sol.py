def solution(a, b, n):
    answer = 0
    while n >= a :
        answer += n//a * b #추가로 얻는 콜라병수
        n = n//a * b + n%a # 추가로 얻은 콜라병 + 나머지

    return answer