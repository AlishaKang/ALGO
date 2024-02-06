def solution(a, b):
    if a < b:
        return sum(list(range(a,b+1)))
    elif a > b:
        return sum(list(range(b,a+1)))
    else: 
        return a
    
print(solution(3,5))