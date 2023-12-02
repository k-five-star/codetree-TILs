#include <stdio.h>
#define SIZE 100

int A[SIZE + 1];
void f(int seq[][2], int m);

int main() {
    int n, m;
    int i;
    int seq[SIZE + 1][2];

    scanf("%d %d", &n, &m);

    for(i = 0; i < n; i++) {
        scanf("%d ", &A[i]);
    }

    for(i = 0; i < m; i++) {
        scanf("%d %d", &seq[i][0], &seq[i][1]);
    }

    f(seq, m);

    return 0;
}

void f(int seq[][2], int m) {
    int i, j;
    int sum = 0;

    for(i = 0; i < m; i++) {
        sum = 0;

        for(j = seq[i][0] - 1; j <= seq[i][1] - 1; j++) {
            sum += A[j];
        }

        printf("%d\n", sum);
    }
}