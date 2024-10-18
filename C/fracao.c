#include <stdio.h>

int reduzfracao (int num, int den){
    int temp;
    while (den != 0 ) {
        temp = den;
        den = num % den;
        num = temp;
    }
    return num;
}
int main (){
    typedef struct{
        int num;
        int den;
    }Tfracao;
    Tfracao X;
    printf("Digite os valores\n");
    scanf ("%d", &X.num);
    do{
        scanf("%d", &X.den);
    }while(X.den == 0);
    if(X.num == 0){
        printf("A fracao irredutivel e %d/%d\n", X.num, X.den);
        return 0;
    }
    int mdc = reduzfracao(X.num, X.den);
    X.num = X.num/mdc;
    X.den = X.den / mdc;
    printf("A fracao irredutivel e %d/%d\n", X.num, X.den);
    return 0;
}