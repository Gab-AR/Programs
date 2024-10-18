#include <stdio.h>
int main() {
    int macas; 
    float custo; 
    printf("Digite a quatidade de maças compradas: ");
    scanf("%d", &macas);
    if (macas<12)
        (custo= macas * 2.30);
    else
        (custo= macas*2);
    printf("O valor total deu %.2f ", custo);
    return 0;
}
    