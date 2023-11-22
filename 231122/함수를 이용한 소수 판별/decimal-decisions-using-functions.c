#include <stdio.h>
int summ(int a, int b);
int isPrime(int n);
int main() {
    int a, b;

    scanf("%d %d", &a, &b);

    printf("%d", summ(a, b));
    return 0;
}

int summ(int a, int b) {
    int i, sum = 0;

    for(i = a; i <= b; i++) {
        if(isPrime(i)) {
            sum += i;
        }
    }

    return sum;
}

int isPrime(int n) {
    int i;

    if(n == 1)
        return 0;

    for(i = 2; i <= n / 2; i++) {
        if(n % i == 0) {
            return 0;
        }
    }

    return 1;
}