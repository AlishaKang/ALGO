import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    line = list(input())

    def check(line):
        stack = []
        for char in line:
            if char == '(' or char == '{':
                stack.append(char)
            elif char == ')' or char == '}':
                if not stack:
                    return 0
                elif char == ')' and stack.pop() != '(':
                    return 0
                elif char == '}' and stack.pop() != '{':
                    return 0
        # 여는 괄호가 남아있으면 0, 없으면 1
        if stack:
            return 0 
        return 1
    
    print("#{} {}".format(tc, check(line)))
