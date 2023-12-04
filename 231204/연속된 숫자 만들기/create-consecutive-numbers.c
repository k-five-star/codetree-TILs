#include <stdio.h>
int main() {
    int small, mid, big;
    int temp;
    int t1, t2;
    int cnt = 0;
    int ts, tm, tb, avg;



    scanf("%d %d %d", &small, &mid, &big);
    ts = small;
    tm = mid;
    tb = big;

    while(mid - small > 1 || big - mid > 1) {
        cnt ++;

        t1 = mid - small;
        t2 = big - mid;
        

        if(t2 >= t2 || mid - small <= 1) { //small과 mid 틈이 더 크니, big과 mid사이에 small이 들어간다. 새로운 것은 그러면 mid 중간 big
            avg = big + mid;
            small = mid;
            mid = mid + 1;
        }

        else if(2 <= t2 || big - mid <= 1) { // 그 반대. 새로운 것은 small 중간 mid
            avg = small + mid;
            big = mid;
            mid = mid -  2;
        }
    }
    
    printf("%d\n", cnt);
    cnt = 0;
    big = tb;
    small = ts;
    mid = tm;

    while(mid - small > 1 || big - mid > 1) {
        cnt++;

        t1 = mid - small;
        t2 = big - mid;

        if(t1 >= t2 || big - mid <= 1) { //small과 mid 틈이 더 크니, 과 mid를 교체
           // avg = small + mid;
            big = mid;
            mid = mid - 1;
        }

        else if(t1 >= t2 || mid - small <= 1){
          //  avg = big + mid;
            small = mid;
            mid = mid + 1;
        }


    }

    printf("%d", cnt);
    cnt = 0;
    

    return 0;
}