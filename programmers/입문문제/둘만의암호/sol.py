def solution(s, skip, index):
    answer = ''
    
    for c in s:
        i = ord(c)
        j = index
        while j > 0:
            i += 1
            if i > ord('z'): #ord() 숫자로바꿈
                i = ord('a')
            if chr(i) in skip:
                j += 1
            j -= 1
        answer += chr(i) #chr() 영어로 바꿈
    
    return answer

print(solution("aukks", "wbqd", 5))
