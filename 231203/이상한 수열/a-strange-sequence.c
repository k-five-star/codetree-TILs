#include <stdio.h>
int rec(int n);
int main() {
    int N;

    scanf("%d", &N);

    printf("%d", rec(N));

    return 0;
}

int rec(int n) {
    if(n <= 2)  return n;
    else        return rec(n / 3) + rec(n - 1);
}