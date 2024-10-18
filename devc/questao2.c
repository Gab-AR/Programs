#include <stdio.h>
int main() {
   /* float macas; 
    float preco; 
    printf("Digite a quatidade de maças compradas \n");
    scanf("%d", &macas);
    if (macas<12){
        (preco= macas * 2.30);
    }
    if (macas>= 12){
        (preco= macas*2);
    }
    printf("%.2d", preco); */
   int macas; float custo;
   printf("Digite o número de macas: ");
   scanf("%d", &macas);
   if(macas<12)
	  custo= macas* 2.30;
   else if(macas>=12)
	  custo = macas*2;
   printf("Valor da compra: %.2f\n", custo);
    return 0;
}
