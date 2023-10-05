numbers = range(1, 201)

result = []

for number in range(1,201):
    if number % 7 == 0 and number % 5 != 0:
        result.append(str(number))

print(','.join(result)) #join() 문자열로 합치기
