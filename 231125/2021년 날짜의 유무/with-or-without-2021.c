#include <stdio.h>

int check_month(int n);
int return_last_date(int n);

int main() {
    int M, D;

    scanf("%d %d", &M, &D);

    if(check_month(M)) 
        if (D >= 1 && D <= return_last_date(M))
            printf("Yes");
            return 0;

    printf("No");

    return 0;
}

int check_month(int n) {
    return n >= 1 && n <= 12 ? 1 : 0;
}

int return_last_date(int n) {
    int d[12] = {31, 28, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31};

    return d[n - 1];
}