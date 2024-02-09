# def solution(phone_number):
#     answer = ''

#     for i in range(len(phone_number)):
#         if i < len(phone_number) - 4:
#             answer += '*'
#         else:
#             answer += phone_number[i]
#     return answer

def solution(phone_number):
    length = len(phone_number)
    answer = ""
    answer = "*"*(length-4) + phone_number[-4:]
    return answer

print(solution("01033334444"))