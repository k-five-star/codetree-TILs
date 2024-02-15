#include <stdio.h>
#include <string.h>

int main() {
    //2진수를 문자열 형태로 입력받는다.

    //sum에 2를 곱한다.
    //해당 자리의 수를 더한다.
    //해당 자리를 한칸 높인다.
    //해당 자리가 strlen()과 같아질때까지 반복한다.

    char bin[10];
    int sum = 0;

    scanf("%s",bin);

    for(int i = 0; i < strlen(bin); i++) {
        sum *= 2;
        sum += (bin[i] - '0');
    }

    printf("%d", sum);

    return 0;
}