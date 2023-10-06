import sys
sys.stdin = open('input.txt') #stadard input

char = input()

if char.isalpha(): #isalpha()는 영문만 있으면 True, 아니면 False
    #소문자인 경우
    if char.islower():
        result = char.upper() #upper() 대문자로 변환
    #대문자인 경우
    else:
        result = char.lower() #lower() 소문자로 변환

    print(char, result)
    print(ord(char), ord(result))


    print(f'{char}(ASCII: {ord(char)}) => {result}(ASCII: {ord(result)})')

else:
    print(char)