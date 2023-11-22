#include <stdio.h>

int f(int n);

int main() {
    int a;
    scanf("%d", &a);

    printf("%d", f(a));


    return 0;
}

int f(int n) {
    int sum = 0;

    for(int i = 1; i <= n; i++)
        sum += i;

    return sum / 10;
}