#include <stdio.h>

int main() {
    // 변수 => N, K, 1차원 배열, 반복문용, 최댓값, a, b//
    int N, K;
    int arr[101] = {0};
    int max = -1;
    int a, b;

    // 알고리즘 //

    // N, K 입력받기
    scanf("%d %d", &N, &K);
    // K 번 반복
    while(K--) {
        // 입력 받기
        scanf("%d %d", &a, &b);
        // 반복문 순회하면서
        for(int i = a; i <= b; i++) {
            // 1 더하기
            arr[i]++;
        }
    }
    // 1~N까지 반복문 순회
    for(int i = 1; i <= N; i++) {
        // max보다 크다면
        if(arr[i] > max) {
            // max를 그걸로 설정
            max = arr[i];
        }
    }
    //출력
    printf("%d", max);

    return 0;
}