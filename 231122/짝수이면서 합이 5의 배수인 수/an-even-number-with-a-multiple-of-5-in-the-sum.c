#include <stdio.h>
#include <stdbool.h>
bool is_magic_number(int n);
int main() {
    int n;

    scanf("%d", &n);

    printf(is_magic_number(n) ? "Yes" : "No");

    return 0;
}

bool is_magic_number(int n) {
    if((n % 2 == 0) && ((n / 10 + n % 10) %  5 == 0))
        return true;

    else
        return false;
}