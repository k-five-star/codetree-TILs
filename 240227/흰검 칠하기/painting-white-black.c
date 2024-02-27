#include <stdio.h>
# define SIZE (100*1000)
int white[2 * SIZE + 1] = {0}, black[2 * SIZE + 1] = {0};
char color[2 * SIZE + 1];
void fill_color(int idx, char cmd);

int main() {
    // 변수 : 흰색 카운트 배열, 검은색 카운트 배열, 색 배열, idx, 명령어, n
    int idx = SIZE, white_cnt = 0, black_cnt = 0, gray_cnt = 0, x, n; 
    int from, to;
    char cmd; 

    // 알고리즘 //
    // n을 입력받는다.
    scanf("%d", &n);
    //n 번 반복한다.
    while(n--) {
        // 명령어들 입력받는다.
        scanf("%d %c", &x, &cmd);
        // 최적화
        if(cmd == 'R') {
            from = idx;
            to = idx + x - 1;
            idx = idx + x - 1;
        }
        else if(cmd == 'L') {
            from = idx - x + 1;
            to = idx;
            idx = idx - x + 1;
        }
        // [from, to] 순회
        for(int i = from; i <= to; i++) {
            // 색칠 함수에 넣기
            fill_color(i, cmd);
        }
    }
    // 배열 순회하면서 값에 따라 카운트
    for(int i = 0; i <= 2 * SIZE; i++) {
        if(color[i] == 'B')         black_cnt++;
        else if(color[i] == 'W')    white_cnt++;
        else if(color[i] == 'G')    gray_cnt++;
    }
    // 출력
    printf("%d %d %d", white_cnt, black_cnt, gray_cnt);

    return 0;
}

void fill_color(int idx, char cmd) {
    // 만약 칼라가 회색이라면, 종료
    if(color[idx] == 'G')       
        return;
    // 만약 커맨드가 L이라면 => 흰색으로 변경, 흰색 카운트 증가
    if(cmd == 'L') {
        color[idx] = 'W';
        white[idx]++;
    }
    // 만약 커맨드가 R이라면 => 검은색으로 변경, 검은색 카운트 증가
    if(cmd == 'R') {
        color[idx] = 'B';
        black[idx]++;
    }
    // 만약 흰2검2라면 => 회색으로 변경
    if(white[idx] >= 2 && black[idx] >= 2)
        color[idx] = 'G';
}