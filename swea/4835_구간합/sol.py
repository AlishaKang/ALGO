import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())   #정수의 개수 #구간의 개수
    numbers = list(map(int, input().split()))    

    max_num = 0
    min_num = sum(numbers)

    for i in range(N-M+1):
        s = sum(numbers[i:i+M])
        if s<min_num:
            min_num = s
        if s>max_num:
            max_num = s

        result = max_num - min_num

    print(f'#{tc} {result}')