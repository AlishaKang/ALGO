def solution(n):
    if n == 1:
        return "수"
    else:
        if n%2 == 0:
            return "수박"*(n//2)
        else:
            return "수박"*(n//2)+"수"
        
print(solution(3))