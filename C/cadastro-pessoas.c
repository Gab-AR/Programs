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
int cadastra (int quant, tpessoa vet[]);
void aniversario (int mes, int quant, tpessoa vet[]);
void imprimir (int i, tpessoa vet[]);

int main (){
    
    tpessoa vet[200];
    int opcao;
    char email[80];
    int data;
    int achar;
    int cadastro;
    int quant = 0;
    printf("|---------------CADASTRO DE PESSOAS---------------|\n");
    //printf("\n");
    
    do{
        do{
        printf("\n");
        printf("|------------------MENU PRINCIPAL-----------------|\n");
        printf("|Escolha uma opcao abaixo:                        |\n");
        printf("|                                                 |\n");
        printf("|1-Cadastrar                                      |\n");
        printf("|2-Localizar                                      |\n");
        printf("|3-Aniversariantes do mes                         |\n");
        printf("|0-Sair                                           |\n");
        printf("|-------------------------------------------------|\n");
        printf("\n");
        scanf("%d", &opcao);
        }while(opcao < 0 || opcao > 3);

        switch (opcao){
        case 1:
            printf("|--------------------CADASTRAR--------------------|\n");
            cadastro = cadastra(quant, vet);
            if(cadastro == 0){
                printf("|--------------------------------------|\n");
                printf("| Numero maximo de cadastros atingido. |\n");
                printf("|--------------------------------------|\n");
            }
            else if(cadastro == -1){
                printf("|-----------------------|\n");
                printf("| E-mail ja cadastrado. |\n");
                printf("|-----------------------|\n");
            }
            else if(cadastro == 1){
                quant++;
                printf("|---------------------------------|\n");
                printf("| Cadastro realizado com sucesso! |\n");
                printf("|---------------------------------|\n");
            }
            break;
        case 2:
            printf("Digite o e-mail a ser localizado:\n");
            scanf("%s", email);
            achar = localiza(email, quant, vet);
            if(achar >= 0){
                imprimir(achar, vet);
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
            aniversario(data, quant, vet);
            break;
        case 0:
            return 0;
        }
    }while(opcao != 0);
    return 0;
}

int localiza(char email[], int quant, tpessoa vet[]){
    for(int i = 0; i < quant; i++){
        if(strcmp(email, vet[i].email) == 0){
            return i;
        }
    }
    return -1;
}

int cadastra (int quant, tpessoa vet[]){
    char email[80];
    if(quant > 199){
        return 0;
    }
    int achar;
    printf("Digite seu e-mail:\n");
    scanf("%s", email);
    achar = localiza(email, quant, vet);
    if (achar >= 0){
        return -1;
    }
    else{
        strcpy(vet[quant].email, email);
        printf("Digite seu primeiro nome:\n");
        scanf("%s", vet[quant].nome);      
        do{
            printf("Digite o dia do seu aniversario:\n");
            scanf("%d", &vet[quant].niver.dia);
        }while(vet[quant].niver.dia < 1 || vet[quant].niver.dia > 31);        
        do{
            printf("Digite o mes do seu aniversario:\n");
            scanf("%d", &vet[quant].niver.mes);
        }while(vet[quant].niver.mes < 1 || vet[quant].niver.mes > 12);
        return 1;
    }
}

void imprimir(int i, tpessoa vet[]){
    printf("Nome: %s\n",vet[i].nome);
    printf("E-mail: %s\n", vet[i].email);
    printf("Aniversario no dia %d/%d\n", vet[i].niver.dia, vet[i].niver.mes);
    return;
}

void aniversario (int mes, int quant, tpessoa vet[]){
    int cont = 0;
    for(int i = 0; i < quant; i++ ){
        if(vet[i].niver.mes == mes){
            imprimir(i, vet);
            cont++;
        }
    }
    if(cont == 0){
        printf("Nenhum usuario cadastrado faz aniversario nesse mes.\n");
    }
}