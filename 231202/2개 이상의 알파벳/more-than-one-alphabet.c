#include <stdio.h>
#include <string.h>
int isnotonlyone(char s[]);

int main() {
    char str[101];
    scanf("%s", str);

    if(isnotonlyone(str)) 
        printf("Yes");

    else
        printf("No");

    return 0;
}

int isnotonlyone(char s[]) {
    char temp = s[0];
    int i;

    for(i = 1; i < strlen(s); i++) {
        if(temp != s[i]) {
            return 1;
        }
    }

    return 0;
}