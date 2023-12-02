#include <stdio.h>
int rec(int n);
int main() {
    int N;

    scanf("%d", &N);

    printf("%d", rec(N));
    return 0;
}

int rec(int n) {
    if(n == 1)      return 2;
    else if(n == 2) return 4;
    else return     (rec(n - 1) * rec(n - 2)) % 100;
}