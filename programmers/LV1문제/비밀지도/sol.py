def solution(n, arr1, arr2):
    l = []
    L = []
    answer = []
    for i in arr1:
        a = bin(i) 
        if len(a[2:]) == n:
            l.append(a[2:])
        else: 
            l.append('0'*(n - len(a[2:])) + a[2:])
    for j in arr2:
        a = bin(j) 
        if len(a[2:]) == n:
            L.append(a[2:])
        else: 
            L.append('0'*(n - len(a[2:])) + a[2:])
    for b in range(n):
        line = []
        k = l[b]
        g = L[b]
        for c in range(n):
            if k[c] == '1' or g[c] == '1':
                line.append('#')
            else:
                line.append(' ')
        answer.append(''.join(line))

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))