#include <stdio.h>
int main (){
    int par[5];
    int impar[5];
    int teste[15];
    int i, j;
    int par1 = 0, impar1 = 0;
    //RECEBE OS 15 VALORES!!
    for (i = 0; i < 15; i++){
        //printf("teste7\n");
        scanf("%d", &teste[i]);
        //COLOCA OS VALORES NOS VETORES
        for(j=0; j<5; j++){
            //printf("teste8\n");
            //TESTE SE É PAR
            if((teste[i]%2)== 0){
                //printf("teste9\n");
                //TESTE SE O VETOR PAR CHEGOU NO FIM
                par1++;
                if(j !=4){
                    //printf("teste10\n");
                    par[j] = teste[i];
                    break;
                }
                else{
                     //printf("teste11\n");
                    par[j] = teste[i];
                    for(j = 0; j < 5; j++){
                        //printf("teste12\n");
                        printf("par[%d] = %d\n", j, par[j]);
                    }
                    par1 = 0;
                    break;
                } 
            }
            //TESTE SE É ÍMPAR
            else{
                //printf("teste13\n");
                if(i != 15){
                    //TESTE SE O VETOR ÍMPAR CHEGOU NO FIM
                    impar1++;
                    if( j != 4){
                        impar[j] = teste[i];
                        //printf("passou\n");
                    }
                    else{
                        impar[j]= teste[i];
                        //printf("passou2\n");
                        for(j = 0; j < 5; j++){
                            //printf("passou3\n");
                            printf("impar[%d] = %d\n", j, impar[j]);
                        }
                        //printf("passou4\n");
                        j = 0;
                        impar1 = 0;
                    }
                }
                else{
                    impar[j] = teste[i];
                    break;
                }
            }
        }
    }
    //IMPRIMIR OS ULTIMOS VALORES RECEBIDOS NOS VETORES ÍMPAR E PAR
    for(i=0; i<=impar1; i++){
        //printf("passou5\n");
        printf("impar[%d] = %d\n", i, impar[i]);
    }
    for(i=0; i<=par1; i++){
        //printf("passou6\n");
        printf("par[%d] = %d\n", i, par[i]);
    }
    return 0;
}