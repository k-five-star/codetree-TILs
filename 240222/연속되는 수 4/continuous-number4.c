#include <stdio.h>

int main() {
    // var //
    // int type N, int type array, i
    int N, a[1000] = {0};
    //int type ans, cnt
    int ans = 0, cnt = 0;
    // algorithm //
    // input
    scanf("%d", &N);

    for(int i = 0; i < N; i++)
        scanf("%d", &a[i]);
    // traverse array
    for(int i = 0; i < N; i++) {
        // i == 0 or a[i] > a[i - 1]
        if(i == 0 || a[i] > a[i - 1])   cnt++;
        // else
        else                            cnt = 1;
        // update ans
        ans = ans < cnt ? cnt : ans;
    }
    // print
    printf("%d", ans);
    return 0;
}