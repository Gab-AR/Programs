#include <stdio.h>
int main (){
    int par[5];
    int impar[5];
    int teste[15];
    int i, j = -1, k = -1;
    int par1 = -1, impar1 = -1;
    //RECEBE OS 15 VALORES!!
    for (i = 0; i < 15; i++){
        scanf("%d", &teste[i]);
        //COLOCA OS VALORES NOS VETORES
            //TESTE SE É PAR
            if((teste[i]%2)== 0){
                //TESTE SE O VETOR PAR CHEGOU NO FIM
                ++j;
                par1++;
                if(j !=4){
                    par[j] = teste[i];
                }
                else{
                    par[j] = teste[i];
                    for(j = 0; j < 5; j++){
                        printf("par[%d] = %d\n", j, par[j]);
                    }
                    j = -1;
                    par1 = -1;
                } 
            }
            //TESTE SE É ÍMPAR
            else{
                //TESTE SE O VETOR ÍMPAR CHEGOU NO FIM
                ++k;
                impar1++;
                if( k != 4){
                    impar[k] = teste[i];
                }
                else{
                    impar[k]= teste[i];
                    for(k = 0; k < 5; k++){
                        printf("impar[%d] = %d\n", k, impar[k]);
                    }
                    k = -1;
                    impar1 = -1;
                }
            }
    }
    //IMPRIMIR OS ULTIMOS VALORES RECEBIDOS NOS VETORES ÍMPAR E PAR
    for(i=0; i<=impar1; i++){
        printf("impar[%d] = %d\n", i, impar[i]);
    }
    for(i=0; i<=par1; i++){
        printf("par[%d] = %d\n", i, par[i]);
    }
    return 0;
}