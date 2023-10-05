import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    char = input()

    if char.islower(): #islower()는 소문자인지 True/False로 확인
        print(f'#{tc} {char}는 소문자입니다.')
    else:
        print(f'#{tc} {char}는 대문자입니다.')