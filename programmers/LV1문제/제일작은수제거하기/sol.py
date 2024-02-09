def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        a = min(arr)
        arr.remove(a)        
        return arr


print(solution([4,3,2,1]))
print(solution([10]))