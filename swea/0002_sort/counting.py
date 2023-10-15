my_list = [1, 5, 8, 2, 3, 1, 7, 9, 3, 5, 7]

counter = [0 for i in range(10)]  

for num in my_list:
    counter[num] += 1

# print(counter)

result = []

for value, count in enumerate(counter):
    # print(value, count)
    for i in range(count):
        result.append(value)

print(result)