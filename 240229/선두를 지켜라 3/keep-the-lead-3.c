#include <stdio.h>
#define SIZE (1000*1000)
int a_pos[SIZE], b_pos[SIZE], gap[SIZE];

int main() {
    int n, m, v, t, cur = 0, ans = 0, i;

    scanf("%d %d", &n, &m);

    // 배열 초기화
    a_pos[0] = 0;
    b_pos[0] = 0;

    while(n--) {
        scanf("%d %d", &v, &t);

        for(i = cur + 1; i <= cur + t && i < SIZE; i++) // SIZE를 초과하지 않도록 보호
            a_pos[i] = a_pos[i - 1] + v;

        cur = i - 1;
    }

    cur = 0;

    while(m--) {
        scanf("%d %d", &v, &t);

        for(i = cur + 1; i <= cur + t && i < SIZE; i++) { // SIZE를 초과하지 않도록 보호
            b_pos[i] = b_pos[i - 1] + v;
            gap[i] = a_pos[i] - b_pos[i];
        }

        cur = i - 1;
    }

    for(i = 1; i <= cur; i++) {
        if (gap[i] != 0 && (i == 1 || gap[i] * gap[i - 1] <= 0))
            ans++;
        else if (gap[i] == 0 && gap[i - 1] != 0)
            ans++;
    }

    printf("%d", ans);

    return 0;
}