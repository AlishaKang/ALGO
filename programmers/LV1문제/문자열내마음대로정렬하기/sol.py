def solution(strings, n):
    return sorted(strings, key=lambda x:(x[n],x))
# sorted(array, key = lambda x : x[0]) 이런식으로 key를 사용해 정렬 가능