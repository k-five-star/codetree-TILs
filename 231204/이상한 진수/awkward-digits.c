#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INT_MIN -99999

int main() {
    int binary[100];
    int length;
    int ans = INT_MIN;
    int i, j, num;

    for (i = 0; i < 100; i++) {
        binary[i] = 0;
    }

    char input[100];
    scanf("%s", input);

    length = strlen(input);

    for (i = 0; i < length; i++) {
        binary[i] = input[i] - '0';
    }

    for (i = 0; i < length; i++) {
        binary[i] = 1 - binary[i];

        num = 0;
        for (j = 0; j < length; j++) {
            num += (1 << (length - j - 1)) * binary[j];
        }

        ans = (ans > num) ? ans : num;

        binary[i] = 1 - binary[i];
    }

    printf("%d\n", ans);

    return 0;
}