#include <stdio.h>

int main() {
    int i, j, N;
    int cnt = 0;

    scanf("%d", &N);

    for(i = 1; i <= N; i++) {
        for(j = 1; j<= N; j++) {
            printf("%d ", (cnt++) % 9 + 1);
        }

        printf("\n");
    }



    return 0;
}