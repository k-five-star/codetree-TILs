#include <stdio.h>
#define SIZE 1000
// 전역 변수 //
// A와 B의 시간당 위치를 기록할 int형의 배열들, 사이즈는 1001, 0으로 초기화
int pos_A[SIZE + 1], pos_B[SIZE + 1];
// 함수 원형 //
int set_pos(int a[], int n);
int main() {
    // 변수 //
    // N, M
    int N, M;
    // ans = 0, 이동 거리 = 0
    int ans = 0, dis = 0;
    // 알고리즘 //
    //입력받기
    scanf("%d %d", &N, &M);
    // set_pos함수 실행
    dis = set_pos(pos_A, N);
    dis = set_pos(pos_B, M);
    // 배열 순회하면서 위치 비교
    for(int i = 1; i <= dis; i++) 
        // 만약 (A[i] - B[i]) * (A[i-1] - B[i-1]) < 0이라면, 선두가 바뀐 것.
        if((pos_A[i] - pos_B[i]) * (pos_A[i - 1] - pos_B[i - 1]) < 0)
            // 카운트++
            ans++;
    //출력
    printf("%d", ans + 1);

    return 0;
}

//set pos 함수
int set_pos(int a[], int n) {
    // 변수 //
    // 속도와 시간 그리고 인덱스
    int v, t, idx = 0;

    //알고리즘 
    //n번의 입력을 받는다.
    for(int i = 0; i < n; i++){
        // 한 번 v와 t를 입력 받고나서
        scanf("%d %d", &v, &t);
        // i를 idx + 1부터 idx + t 까지 갱신시킨다.
        for(int i = idx + 1; i <= idx + t; i++) {
            // 직전 배열의 값(a[i - 1]) + v만큼 새 배열에 저장
            a[i] = a[i - 1] + v;
        }

        idx = i + 1;
    }
    //idx반환
    return idx;
}