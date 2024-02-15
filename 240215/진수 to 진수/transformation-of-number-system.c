#include <stdio.h>
#include <string.h>
int to_dec(char org[], int form);
void to_form(int n, char a[], int form);
int main() {
    // 정수형 배열의 원래 수, 정수형의 원래수 진법, 정수형 배열의 변환수, 정수형의 변환 수 진법
    int org_form, tran_form;
    char org[100], tran[100];
    //정수형의 temp
    int temp, len;

    //입력을 받는다.
    scanf("%d %d", &org_form, &tran_form);
    scanf("%s", org);

    // 일단 10진수로 변환하여 temp에 저장
    temp = to_dec(org, org_form);

    //temp를 다시 변환 진수로 변환하여 배열에 저장
    to_form(temp, tran, tran_form);
    
    //출력은 거꿀로
    for(int i = strlen(tran) - 1; i >= 0; i--) 
        printf("%d", tran[i] - '0');

    return 0;
}

int to_dec(char org[], int form) {
    int sum = 0;
    // 인덱스 끝까지 반복한다.
    for(int i = 0; i < strlen(org); i++) {
        //sum을 form만큼 곱한다.
        sum *= form;
        //sum에 index파트의 그 수를 더한다.
        sum += (org[i] - '0');
    }
    //sum을 반환
    return sum;
}

void to_form(int n, char a[], int form) {
    int idx = 0;
    //n이 0이 될때까지 반복한다.

    if(n == 0) {
        a[idx] = '0';
        return;
    }

    while(n != 0) {
        //n을 form으로 나눈 나머지를 idx의 부분에 적는다.
        a[idx] = n % form + '0';
        //n을 form으로 나누다.
        n /= form;
        //idx를 올린다.
        idx++;
    }
}