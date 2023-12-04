#include <stdio.h>
char a[100][100];

int main() {
    int n, m, k;
    int i, j;

    scanf("%d %d %d", &n, &m, &k);

    for(i = 0; i < n; i++) 
        for(j = 0; j < m; j++)
            scanf(" %c", &a[i][j]);
    
    
    for(i = 0; i < k*n; i++) {
        for(j = 0; j < k*m; j++) {
            printf("%c", a[i / 2][j / 2]);
        }
        printf("\n");
    }


    return 0;
}