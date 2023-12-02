#include <stdio.h>
void rec(int n);
int main() {
    int N;

    scanf("%d", &N);
    rec(N);

    return 0;
}

void rec(int n) {
    if(n == 0) 
        return;
    
    int i;

    printf("%d ", n);
    rec(n - 1);
    printf("%d ",n);
}