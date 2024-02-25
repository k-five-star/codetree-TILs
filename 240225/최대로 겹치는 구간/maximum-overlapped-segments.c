#include <stdio.h>
# define SIZE 200
int main() {
    // 변수 배열(인덱스 음수 가능으로), n, x1x2, ans
    int temp_a[SIZE + 1] = {0};
    int *arr = temp_a + 100;
    int n, x1, x2, ans = -1;

    // 알골

    //n 입력받기
    scanf("%d", &n);
    // n번 반복
    while(n--) {
        // x1 x2 입력받기
        scanf("%d %d", &x1, &x2);
        // [x1, x2) 순회하며 1증가시키기
        for(int i = x1; i < x2; i++) arr[i]++;
    }
    // [-100, 100] 순회하며, 만약 최대값이면 업데이트하기
    for(int i = -100; i <= 100; i++) 
        if(arr[i] > ans)
            ans = arr[i];

    //출력
    printf("%d", ans);
    return 0;
}