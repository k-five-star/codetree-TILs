#include <stdio.h>
int main() {
    int a, c;
    char o;

    scanf("%d %c %d", &a, &o, &c);

    if(o == '+')
        printf("%d %c %d = %d",a, o, c, a + c);

    else if(o == '-')
        printf("%d %c %d = %d",a, o, c, a - c);

    else if(o == '*')
        printf("%d %c %d = %d",a, o, c, a * c);

    else if(o == '/')
        printf("%d %c %d = %d",a, o, c, a / c);

    else
        printf("False");

    return 0;
}