#include <stdio.h>
#define SIZE 250

int a[SIZE][SIZE];
void fill_array(int x1, int y1, int x2, int y2);

int main() {
    // int 좌표들, int N, cnt
    int x1, y1, x2, y2, N, cnt = 0;
    //입력을 받는다.
    scanf("%d", &N);

    // 사각형 개수만큼 반복한다.
    while(N--) {
        //좌표를 입력받는다.
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        //좌표를 전처리한다.
        x1+=100;
        y1+=100;
        x2+=100;
        y2+=100;
        x2--;
        y2--;
        // 배열에 적는 함수 실행
        fill_array(x1, y1, x2, y2);
    }
    //배열에서 색칠된 부분 개수 구하기
    for(int i = 0; i <= 200; i++) for(int j = 0; j <= 200; j++) if(a[i][j]) cnt++;
    //출력
    printf("%d", cnt);
    
    return 0;
}

void fill_array(int x1, int y1, int x2, int y2) {
    for(int i = x1; i <= x2; i++) for(int j = y1; j <= y2; j++) a[i][j] = 1;
}