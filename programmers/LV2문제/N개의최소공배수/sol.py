def solution(arr):
    from math import gcd # 최대공약수를 구하는 gcd() 
    answer = arr[0]                                 

    for num in arr:                                
        answer = answer*num // gcd(answer, num)     

    return answer