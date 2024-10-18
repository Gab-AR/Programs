#include <stdio.h>
int mdc (int a, int b){
    int temp;
    while(b=!0){
        temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
/*int mmc(int num1, int den1, int num2, int den2){
    int den = den1 * den2;
    num1 = (den / den1) * num1;
    num2 = (den / den2) * num2;
}*/
int main() {
    typedef struct {
        int num1;
        int den1;
        int num2;
        int den2;
        int temp;
    } Valores;
    typedef struct {
        int num_final;
        int den_final;
        int mdc;
    } Final;
    Final resultado;
    Valores valor;
    char operador;
    printf("Digite 4 valores, que representam 2 frações:\n");
    scanf("%d%d%d%d", &valor.num1 ,&valor.den1 , &valor.num2, &valor.den2);
    printf("Digite o operador +, -, *, /:\n");
    scanf(" %c", &operador);
    switch (operador){
        case '+':
            resultado.den_final = valor.den1 * valor.den2;
            valor.num1 = valor.num1 * valor.den2;
            valor.num2 = valor.num2 * valor.den1;
            resultado.num_final = valor.num1 + valor.num2;
            resultado.mdc = mdc(resultado.num_final, resultado.den_final);
            resultado.num_final = resultado.num_final / resultado.mdc;
            resultado.den_final = resultado.den_final / resultado.mdc;
            break;
        case '-':
            resultado.den_final = valor.den1 * valor.den2;
            valor.num1 = valor.num1 * valor.den2;
            valor.num2 = valor.num2 * valor.den1;
            resultado.num_final = valor.num1 - valor.num2;
            resultado.mdc = mdc(resultado.num_final, resultado.den_final);
            resultado.num_final = resultado.num_final / resultado.mdc;
            resultado.den_final = resultado.den_final / resultado.mdc;
            break;
        case '*':
            resultado.num_final = valor.num1 * valor.num2;
            resultado.den_final = valor.den1 * valor.den2;
            resultado.mdc = mdc(resultado.num_final, resultado.den_final);
            resultado.num_final = resultado.num_final / resultado.mdc;
            resultado.den_final = resultado.den_final / resultado.mdc;
            break;
        case '/':
            valor.temp = valor.num2;
            valor.num2 = valor.den2;
            valor.den2 = valor.temp;
            resultado.num_final = valor.num1 * valor.num2;
            resultado.den_final = valor.den1 * valor.den2;
            resultado.mdc = mdc(resultado.num_final, resultado.den_final);
            resultado.num_final = resultado.num_final / resultado.mdc;
            resultado.den_final = resultado.den_final / resultado.mdc;
            break;
        default:
            printf("Operador invalido\n");
            break;
    }


    return 0;
}
