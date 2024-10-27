#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

# 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
bool solution(const char* s) {
    bool answer = true;
    int stack = 0;
    int len = strlen(s);

    for(int i=0;i<len;i++){
        if(s[i]=='('){
            stack++;
        }else{
            if(stack==0) return false;
            stack--;
        }
    }
    if(stack>0) answer = false;
    return answer;
}