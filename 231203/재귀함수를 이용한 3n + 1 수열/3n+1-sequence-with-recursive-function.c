#include <stdio.h>
int rec(int n);
int main() {
    int N;

    scanf("%d", &N);

    printf("%d", rec(N));
    return 0;
}

int rec(int n) {
    if(n == 1) 
        return 0;

    if(n % 2 == 0) 
        return rec(n / 2) + 1;

    else
        return rec(3 * n + 1) + 1;
}