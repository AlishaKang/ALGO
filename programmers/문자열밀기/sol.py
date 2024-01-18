# def solution(A, B):
#     cnt = 0
#     if A != B:
#         while cnt < len(A):
#             cnt += 1
#             a=A[-1]
#             A=A[:-1]
#             if a+A == B:
#                 return cnt
#         if cnt == len(A):
#             return -1
#     else: #A=B경우
#         return 0
def solution(A, B):
    B *= 2
    if A in B:
        return B.find(A)
    else:
        return -1    
   
print(solution("hello", "ohell"))
print(solution("apple", "elppa"))