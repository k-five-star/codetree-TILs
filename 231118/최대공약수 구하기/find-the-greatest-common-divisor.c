#include <stdio.h>

int main() {
    //유클리드 호제법 사용

    int big, small, temp;

    scanf("%d %d", &big, &small);

    if(big < small) {
        temp = big;
        big = small;
        small = temp;
    }

    while(big % small != 0) {
        temp = big % small;

        if(temp < small) {
            big = small;
            small = temp;
        }

        else
            big = temp;
    }

    printf("%d", small);
    
    return 0;
}