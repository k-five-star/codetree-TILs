#include <stdio.h>
#define MINPERDAY 60*24
#define MINPERHOUR 60
#define MINPERMIN 1
int main() {
    int a, b, c;
    int delta_day, delta_hour, delta_min;
    int elapsed_min = 0;

    scanf("%d %d %d", &a, &b, &c);

    delta_day = a - 11;
    delta_hour = b - 11;
    delta_min = c - 11;

    elapsed_min = delta_day * MINPERDAY + delta_hour * MINPERHOUR + delta_min * MINPERMIN;

    printf("%d", elapsed_min>=0?elapsed_min:-1);

    return 0;
}