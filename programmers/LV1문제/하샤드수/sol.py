def solution(n):
    a = sum(int(i) for i in str(n))
    
    if n % a == 0:
        return True
    else:
        return False
    
print(solution(10))