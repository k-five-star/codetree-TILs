#include <stdio.h>

int main() {
    // 변수 : n, x1 x2, 배열, ans
    int n, x1, x2, ans = -1;
    int a[101] = {0};
    // 알고리즘 //
    // n 입력받음 
    scanf("%d", &n);
    // n 번 반복
    while(n--) {
        // x1 x2 입력받음
        scanf("%d %d", &x1, &x2);
        // 배열 순회 [x1, x2]
        for(int i = x1; i <= x2; i++) 
            // a[i]++
            a[i]++;
    }
    // 배열 순회
    for(int i = 1; i <= 100; i++)
        // 젤 크다
        if(a[i] > ans)
            //저장
            ans = a[i];
    //프린트
    printf("%d", ans);
    return 0;
}