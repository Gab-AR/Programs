#include <stdio.h>
int main(){
    float matriz[12][12];
    int i,j,k = 11;
    char operador;
    float soma = 0;
    scanf(" %c", &operador);
    for(i=0; i<12; i++){
        for(j=0; j<12; j++){
            scanf("%f", &matriz[i][j]);
        }
    }
    for(i=0; i<11; i++){
        for(j = 0; j<k; j++){
           soma = soma + matriz[i][j];
        }
        k--;
    }

    switch (operador){
    case 'S':
        printf("%.1f\n", soma);
        break;
    case 'M':
        printf("%.1f\n", soma/66);
        break;
    default:
        break;
    }
    return 0;
}