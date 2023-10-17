# 부분집합들 출력하기

# numbers = list(range(1,5))

# n = len(numbers)

# for i in range(1<<n):
#     # print(i)

#     temp = []
#     for j in range(n):
#         # print(i, bin(i), bin(1<<j))
#         if i & (1<<j):
#             temp.append(numbers[j])

#     print(temp)

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1 + T):
    N, K = list(map(int, input().split())) #원소겟수 #부분집합의 합
    numbers = list(range(1, 13))
    
    count = 0

    for i in range(1 << len(numbers)):
        temp = []
        for j in range(len(numbers)):
            if i & (1 << j):
                temp.append(numbers[j])

        if len(temp) == N and sum(temp) == K:
            count += 1
    
    print(f'#{tc} {count}')
