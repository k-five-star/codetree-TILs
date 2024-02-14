#include <stdio.h>
#define MONTH 12
int main() {
    int lastdayOfMonth[MONTH + 1] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int m1, d1, m2, d2;
    int month, day;
    int elapsedDate = 0;

    scanf("%d %d %d %d", &m1, &d1, &m2, &d2);
    month = m1;
    day = d1;

    while(!(month == m2 && day == d2)) {
        elapsedDate++;
        day++;

        if(day > lastdayOfMonth[month]) {
            day = 1;
            month++;
        }
    }

    printf("%d", elapsedDate+1);

    return 0;
}