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
    int i = 0, j = 0;

    while(i < strlen(s) && j < strlen(sub)) {
        if(s[i] == sub[j]) {
            i++;
            j++;
        }

        else {
            if(j != 0) {
                j = 0;
            }
            else {
                i++;
                j = 0;
            }
        }
    }

    if(j == strlen(sub)) 
        return i - j;

    else
        return -1;
}