blood_list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

blood_dict = {
    'A': 0,
    'O': 0,
    'B': 0,
    'AB': 0,
}

for blood in blood_list:
    blood_dict[blood] += 1

print(blood_dict)