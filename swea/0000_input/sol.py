import sys
sys.stdin = open('input.txt')

TC = int(input()) #TestCase

for i in range(TC):
    num = int(input())

    if num % 2 == 1:
        print('홀수')
    else:
        print('짝수')

# 1차원 리스트 input받기
# numbers = input().split()

# print(numbers)
# print(type(numbers))

# for number in numbers:
#     int_num = int(number)

#     if int_num % 2 == 1:
#         print(f'{int_num}은 홀수입니다.')

numbers = list(map(int, input().split()))

for number in numbers:
    if number % 2 == 1:
        print(f'{numbers}은 홀수입니다.')



# 2차원 리스트 입력
N = int(input()) #줄 수
matrix = []

for i in range(N):
    numbers = list(map(int, input().split()))
    matrix.append(numbers)

# for row in matrix:
#     for item in row:
#         print(row)

# 행 우선 반복 (index접근)
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print(i, j, matrix[i][j])

# 열 우선 반복 (index접근)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(i, j, matrix[j][i])