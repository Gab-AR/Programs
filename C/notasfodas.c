#include <stdio.h>
int main(){
float nota, soma_notas = 0, maior_nota = 0, menor_nota = 10, soma_maior7 = 0;
int cont_menor4 = 0, cont_maior7 = 0, cont_total = 0, operador;
do{
    do{ // Obrigando esse imbecil a digitar direito
    printf("Digite uma nota: \n");
    scanf(" %f", &nota);} while(nota < 0 || nota > 10);
cont_total++;
soma_notas = soma_notas + nota;
if (nota >= 7){
    soma_maior7 = soma_maior7 + nota;
    if (nota >= 9){
        printf("Nota Excelente!\n");
        cont_maior7++;
    }
    else{
        cont_maior7++;
    }
}
else{
    printf("Estude mais!\n");
}
if (nota < 4)
    cont_menor4++;
if (nota > maior_nota)
    maior_nota = nota;
if (nota < menor_nota)
    menor_nota = nota;

printf("Digite um numero diferente de 0 se quiser digitar outra nota.\n");
scanf(" %d", &operador);
}while(operador != 0);
// Resultados
printf("Media total = %.2f\n", (soma_notas / cont_total));
if (cont_maior7 > 0)
    printf("Media dos numeros maiores que 7: %.2f\n", (soma_maior7 / cont_maior7));
else{ printf("Nao ha notas maiores que 7.\n"); }

printf("Numero de notas menor que 4: %d\n", cont_menor4);
printf("A maior nota foi: %.2f\n", maior_nota);
printf("A menor nota foi: %.2f\n", menor_nota);

    return 0;
}