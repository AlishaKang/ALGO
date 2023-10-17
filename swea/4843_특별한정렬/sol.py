import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1 + T):
    N = int(input())
    numbers = list(map(int, input().split()))

    result = []

        #가장큰수 찾아 넣고 리스트에서 지우기
    while True:
        max_num = 0
        for i in range(len(numbers)):
            if max_num < numbers[i]:
                max_num = numbers[i]
        result.append(max_num)
        numbers.remove(max_num)

        min_num = 1000000000
        for j in range(len(numbers)):
            if numbers[j] < min_num:
                min_num = numbers[j]
        result.append(min_num)
        numbers.remove(min_num)

        if len(result) == 10:
            break
        
    # print(result)
    temp = list(map(str, result))
    result = ' '.join(temp)
    print(result)   