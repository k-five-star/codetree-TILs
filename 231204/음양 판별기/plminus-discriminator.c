#include <stdio.h>

int main() {
    int n;

    scanf("%d", &n);

    while(n--) {
        int a;

        scanf("%d", &a);

        if(a > 0)   printf("plus\n");
        if(a < 0)   printf("minus\n");
        if(a == 0)  printf("zero\n");
    }
    return 0;
}