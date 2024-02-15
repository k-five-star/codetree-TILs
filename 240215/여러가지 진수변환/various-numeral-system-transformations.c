#include <stdio.h>
#include <string.h>
void trans(int N, int form, char ans[]);
int main() {
    // 정수형 N, 문자열의 변경된 수ans, 정수형의 진수 form
    int N, form;
    char ans[10];
    // 진수 변환 함수

    //입력 받는다.
    scanf("%d %d", &N, &form);

    //진수를 변환한다.
    trans(N, form, ans);

    //거꾸로 출력한다.
    for(int i = strlen(ans) - 1; i >= 0; i--)
        printf("%c", ans[i]);
    return 0;
}

//진수 변환 함수 : void형, 포인터로 ans 배열에 접근
void trans(int N, int form, char ans[]) {
    //0이라면 0으로
    if(N == 0) {
        ans[0] == '0';
        return;
    }

    int idx = 0;

    while(N != 0) {
        //form으로 N을 나눈 나머지를 idx파트에 적는다.
        ans[idx] = N % form + '0';
        //N은 form으로 나눈다.
        N /= form;
        //idx를 올린다.
        idx++;
    }
}