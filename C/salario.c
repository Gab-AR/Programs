#include <stdio.h>
int main (){
    float salario, NVsalrio, reajuste;
    scanf("%f", &salario);
    if (salario >= 0 && salario <= 400.00){
        NVsalrio = salario*1.15;
        reajuste = NVsalrio - salario;
        printf("Novo salario: %.2f\n", NVsalrio);
        printf("Reajuste ganho: %.2f\n", reajuste);
        printf("Em percentual: 15 %\n");
    }
    else if (salario > 400.00 && salario <= 800.00){
        NVsalrio = salario*1.12;
        reajuste = NVsalrio - salario;
        printf("Novo salario: %.2f\n", NVsalrio);
        printf("Reajuste ganho: %.2f\n", reajuste);
        printf("Em percentual: 12 %\n");
    }
    else if (salario > 800.00 && salario <= 1200.00){
        NVsalrio = salario*1.10;
        reajuste = NVsalrio - salario;
        printf("Novo salario: %.2f\n", NVsalrio);
        printf("Reajuste ganho: %.2f\n", reajuste);
        printf("Em percentual: 10 %\n");
    }
    else if (salario > 1200.00 && salario <= 2000.00){
        NVsalrio = salario*1.07;
        reajuste = NVsalrio - salario;
        printf("Novo salario: %.2f\n", NVsalrio);
        printf("Reajuste ganho: %.2f\n", reajuste);
        printf("Em percentual: 7 %\n");
    }
    else{
        NVsalrio = salario*1.04;
        reajuste = NVsalrio - salario;
        printf("Novo salario: %.2f\n", NVsalrio);
        printf("Reajuste ganho: %.2f\n", reajuste);
        printf("Em percentual: 4 %\n");
    }
    return 0;
}