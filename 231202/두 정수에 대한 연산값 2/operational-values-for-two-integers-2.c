#include <stdio.h>
void f(int a[]);
int main() {
    int a[2];

    scanf("%d %d", &a[0], &a[1]);
    f(a);

    printf("%d %d", a[0], a[1]);
    return 0;
}

void f(int a[]) {
    if(a[0] > a[1]) {
        a[0] *= 2;
        a[1] += 10;
    }

    else {
        a[0] += 10;
        a[1] *= 2;
    }
}