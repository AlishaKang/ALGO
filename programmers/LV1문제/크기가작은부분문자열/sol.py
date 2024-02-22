def solution(t, p):
    list = []
    a = len(p)
    cnt = 0
    for i in range(len(t)): # 슬라이싱한 숫자의 길이가 p길이 미만이면 append 안 하기
        if len(t[i:i+a]) == a:
            list.append(t[i:i+a]) 
    for j in list:
        if j <= p:
            cnt += 1
    return cnt

print(solution("3141592","271"))