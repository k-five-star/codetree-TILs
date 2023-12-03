#include <stdio.h>

typedef struct {
    char code[100];
    char point;
    int time;
}Secret;

int main() {
    Secret s1;

    scanf("%s %c %d", s1.code, &s1.point, &s1.time);

    printf("secret code : %s\n", s1.code);
    printf("meeting point : %c\n", s1.point);
    printf("time : %d\n", s1.time);
    return 0;
}