#include <stdio.h>
int main(){
    float matriz[12][12];
    int coluna;
    int i,j;
    char operador;
    float soma = 0;
    scanf("%d", &coluna);
    scanf(" %c", &operador);
    for(i=0; i<12; i++){
        for(j=0; j<12; j++){
            scanf("%f", &matriz[i][j]);
            if(j == coluna)
                soma = soma + matriz[i][j];
        }
    }
    
    switch (operador){
    case 'S':
        printf("%.1f\n", soma);
        break;
    case 'M':
        printf("%.1f\n", soma/12);
        break;
    default:
        break;
    }
    return 0;
}