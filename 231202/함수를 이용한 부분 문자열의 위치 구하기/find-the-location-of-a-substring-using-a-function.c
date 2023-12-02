#include <stdio.h>
#include <string.h>
char s[1001];
char sub[1001];
int isSub();

int main() {
    scanf("%s", s);
    scanf("%s", sub);

    printf("%d", isSub());  
    return 0;
}

int isSub() {
    int sub_idx = 0;
    int i;
    for(i = 0; i < strlen(s); i++) {
        if(s[i] == sub[sub_idx])
            sub_idx ++;
        
        else
            sub_idx = 0;

        if(sub_idx == strlen(sub))
            return i - sub_idx + 1;
    }

    return -1;
}