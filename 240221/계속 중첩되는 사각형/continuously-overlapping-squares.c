#include <stdio.h>
#define SIZE 200
int arr[SIZE + 1][SIZE + 1];
void fill_arr(int x1, int y1, int x2, int y2, int color);
int main() {
    //변수//
    // int형 전체 2차원 배열(201 201), int형 사각형 개수, int형 좌표 받을 것
    int N, x1, x2, y1, y2;
    // int형 cnt
    int cnt = 0;

    //알고리즘//
    
    //횟수를 입력 받는다.
    scanf("%d", &N);
    //횟수만큼 반복한다. 1~N까지 실행하고 N+1일때 멈춤
    for(int i = 1; i <= N; i++) {
        //좌표를 입력받는다. 
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        //좌표를 전처리한다.
        x1 += 100;
        y1 += 100;
        x2 += 100;
        y2 += 100;
        //지금이 홀수번째면 빨강, 짝수번째면 파랑인지를 파악해서, 필드를 갱신하는 함수 실행
        if(i % 2 == 1)  fill_arr(x1, y1, x2, y2, 1);
        else            fill_arr(x1, y1, x2, y2, -1);
    }
    //전체 배열을 순회하며 조사한다.
    for(int i = 0; i <= SIZE; i++)
        for(int j = 0; j <= SIZE; j++)
            //만약 파란색이면 cnt++
            if(arr[i][j] == -1)
                cnt++;
    //출력한다.
    printf("%d", cnt);
    return 0;
}

//색칠하는 함수
void fill_arr(int x1, int y1, int x2, int y2, int color) {
    //변수//
    //int 형 순회할 변수 2개
    int i, j;
    //알고리즘//

    //순회
    for(i = x1; i < x2; i++) 
        for(j = y1; j < y2; j++)
        //채워넣기
        arr[i][j] = color;

    return;
}