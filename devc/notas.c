#include <stdio.h>
int main() {
    float nota1, nota2, nota3, media;
    printf("Digite as 3 notas:\n");
    scanf("%f%f%f", &nota1, &nota2, &nota3);
    media = (nota1+nota2+nota3)/3;
    printf("A media do aluno: %.2f \n", media);
    if (media>= 7){
        printf("APROVADO");
    }
    if (media < 4){
        printf("REPROVADO");
    }
    if (media>= 4 && media<7){
	 printf("EXAME FINAL");
    }

    return 0;
}
