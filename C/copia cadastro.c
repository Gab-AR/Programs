#include <stdio.h>
#include <string.h>
typedef struct{
        int dia;
        int mes;
}tdata;

typedef struct{
    char nome[80];
    char email[80];
    tdata niver;
}tpessoa;

int localiza (char email[], int quant, tpessoa vet[]);
int cadastra (int quant, tpessoa *vet[]);
int aniversario (int mes, tpessoa vet[]);
void imprimir ();

int main (){
    
    tpessoa vet[200];
    int opcao;
    int data;
    int achar;
    int cadastro;
    int quant = 0;
    do{
        do{
        printf("Escolha uma opcao abaixo:\n");
        printf("1-Cadastrar\n");
        printf("2-Localizar\n");
        printf("3-Aniversariantes do mês\n");
        printf("0-Sair\n");
        scanf("%d", &opcao);
        }while(opcao < 0 || opcao > 3);

        switch (opcao){
        case 1:
            cadastro = cadastra(quant, &vet[quant]);
            quant++;
            printf("Cadastro realizado com sucesso!\n");
            break;
        case 2:
            printf("Digite o e-mail a ser localizado:\n");
            scanf("%s", vet[quant].email);
            achar = localiza(vet[quant].email, quant, &vet[quant]);
            if(achar >= 0){
                printf("%s\n",vet[achar].nome);
                printf("Aniversario no dia %d/%d\n", vet[achar].niver.dia, vet[achar].niver.mes);
            }
            else{
                printf("E-mail nao cadastrado.\n");
            }
            break;
        case 3:
            do{
                printf("Digite o mes de aniversario (1 a 12):\n");
                scanf("%d", &data);
            }while(data < 1 || data > 12 );

            break;
        case 0:
            return 0;
        }
    }while(opcao != 0);
    return 0;
}

int localiza(char email[], int quant, tpessoa vet[]){
    for(int i = 0; i < quant; i++){
        if(strcmp(vet[quant].email, vet[i].email) == 0){
            return i;
        }
    }
    return -1;
}

int cadastra (int quant, tpessoa *vet[]){
    if(quant > 199){
        return 0;
    }
    int achar;
    printf("Digite seu e-mail:\n");
    scanf("%s", vet[quant]->email);
    achar = localiza(vet[quant]->email, quant, vet[quant]);
    if (achar >= 0){
        printf("E-mail ja cadastrado.\n");
        return -1;
    }
    else{
        printf("Digite seu nome completo:\n");
        fgets(vet[quant]->nome, 80, stdin);
        printf("Digite o dia e o mes do seu aniversario:\n");
        scanf("%d%d", &vet[quant]->niver.dia, &vet[quant]->niver.mes);
        return 1;
    }
}

int aniversario (int mes, tpessoa vet[]){

}