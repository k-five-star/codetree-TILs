#include <stdio.h>
char itoa(int n);
int main() {
    //10진수를 2로 나눈 나머지를 적는다.
        //문자열의 인덱스부분에 적는다.
        //인덱스를 뒤로 한칸 물린다.
    //10진수를 2로 나눈다.
    //그걸 10진수가 0이 될때까지 반복한다.

    //문자열을 인덱스-1에서 0까지 읽는다.

    int dec;
    int idx = 0;
    char bin[30];

    scanf("%d", &dec);

    if(dec == 0) {
        bin[idx] = '0';
        idx++;
    }

    while(dec > 0) {
        bin[idx] = itoa(dec % 2);
        idx++;

        dec /= 2;
    }

    for(int i = idx - 1; i >= 0; i--) 
        printf("%c", bin[i]);


    return 0;
}

char itoa(int n) {
    if(n == 1)
        return '1';

    else if(n == 0) 
        return '0';
}