#include <stdio.h>

int check_prime_number(int n);
int sum_digit(int n);

int main() {
    int a, b, i;
    int cnt = 0;

    scanf("%d %d", &a, &b);

    for(i = a; i <= b; i++) 
        if(check_prime_number(i) == 1 && sum_digit(i) % 2 == 0)
            cnt++;
    
    printf("%d", cnt);

    return 0;
}

int check_prime_number(int n) {
    int i;

    if(n == 1)
        return 0;

    for(i = 2; i * i <= n; i++)
        if(n % i == 0) 
            return 0;

    return 1;
}

int sum_digit(int n) {
    int sum = 0;
    
    while(n) {
        sum += n % 10;
        n /= 10;
    }

    return sum;
}