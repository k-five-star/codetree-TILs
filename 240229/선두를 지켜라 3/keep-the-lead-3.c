#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 1000000 // 충분히 큰 사이즈를 정의합니다.

// cmd_arr에 기반한 위치를 계산하는 함수
int* gen_pos_per_sec(int n, int cmd_arr[][2]) {
    int* pos = (int*)malloc(MAX_SIZE * sizeof(int));
    int pos_size = 1; // 현재 pos 배열의 크기
    pos[0] = 0; // 초기 위치는 0

    for (int i = 0; i < n; ++i) {
        int v = cmd_arr[i][0];
        int t = cmd_arr[i][1];
        for (int j = 0; j < t; ++j) {
            if (pos_size < MAX_SIZE) {
                pos[pos_size] = pos[pos_size - 1] + v;
                ++pos_size;
            }
        }
    }
    return pos;
}

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    
    int A_cmds[N][2], B_cmds[M][2];
    
    // A_cmds 입력 받기
    for (int i = 0; i < N; ++i) {
        scanf("%d %d", &A_cmds[i][0], &A_cmds[i][1]);
    }
    
    // B_cmds 입력 받기
    for (int i = 0; i < M; ++i) {
        scanf("%d %d", &B_cmds[i][0], &B_cmds[i][1]);
    }
    
    int* A_pos = gen_pos_per_sec(N, A_cmds);
    int* B_pos = gen_pos_per_sec(M, B_cmds);
    
    int ans = 0;
    
    for (int i = 1; i < MAX_SIZE; ++i) {
        int gap = A_pos[i] - B_pos[i];
        
        if (gap != 0) {
            if (i == 1 || gap * (A_pos[i-1] - B_pos[i-1]) <= 0) {
                ans++;
            }
        } else if (A_pos[i-1] - B_pos[i-1] != 0) {
            ans++;
        }
    }
    
    printf("%d\n", ans);
    
    free(A_pos);
    free(B_pos);
    
    return 0;
}