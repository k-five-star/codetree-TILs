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
        return 1;
    
    return n + rec(n - 1);
}