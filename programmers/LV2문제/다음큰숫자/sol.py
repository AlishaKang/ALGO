# solution(n) {
#     a = bin(int n)
#     b = a.count(1)
#     for i in range(1,1000000,1):
#         if bin(n+i).count(1) == b: 
#             return n+i
# }

def solution(n):
    
    #자연수 n을 이진수로 변환했을 때 1의 갯수
    cnt1 = bin(n)[2:].count("1")
    
    #자연수 n을 1씩 증가시킨다.
    while True:
        n += 1
        if cnt1 == bin(n)[2:].count("1"):
            break

    return n

print(solution(78))