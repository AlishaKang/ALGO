import sys
sys.stdin = open('input.txt') #stadard input

char = input()

if char.isa

#소문자인 경우
if char.islower():
    result = char.upper()
#대문자인 경우
else:
    result = char.lower()

print(char, result)
print(ord(char), ord(result))


print(f'{char}(ASCII: {ord(char)}) => {result}(ASCII: {ord(result)})')

else:
    print(char)