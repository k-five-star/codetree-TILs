#include <stdio.h>

int main() {
    int dx[4] = {0, 1, 0, -1};  // 방향에 따른 x의 변화량
    int dy[4] = {1, 0, -1, 0};  // 방향에 따른 y의 변화량
    // 0 동 1 서 2 남 3 북
    int n, num, x = 0, y = 0, i;
    char cmd;

    scanf("%d", &n);
    getchar();

    for(i = 0; i < n; i++) {
        scanf(" %c %d", &cmd, &num);

        if (cmd == 'N') {
    x += num * dx[0];
    y += num * dy[0];
} else if (cmd == 'E') {
    x += num * dx[1];
    y += num * dy[1];
} else if (cmd == 'S') {
    x += num * dx[2];
    y += num * dy[2];
} else if (cmd == 'W') {
    x += num * dx[3];
    y += num * dy[3];
}
    }

    printf("%d %d\n", x, y);
    return 0;
}