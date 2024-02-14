#include <stdio.h>

int main() {
    int a, b, c, d;
    int total = 0;
    int min, hour;

    scanf("%d %d %d %d", &a, &b, &c, &d);
    hour = a;
    min = b;

    while(!(hour == c && min == d)) {
        total++;
        min++;

        if(min == 60) {
            min = 0;
            hour++;
        }
    }

    printf("%d", total);
    
    return 0;
}