def solution(numbers):
    a = list(range(0,10))
    for element in numbers:
        a.remove(element)
    return sum(a)
        
    
print(solution([1,2,3,4,6,7,8,0]))

