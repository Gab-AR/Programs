#include <stdio.h>
int main (){
    int hora_inicio, hora_fim, min_inicio, min_fim, total_horas, total_min;
    scanf("%i %i %i %i", &hora_inicio, &min_inicio, &hora_fim, &min_fim);
    if (min_inicio <= min_fim)
        total_min = min_fim - min_inicio;
    else
        total_min = 60 - (min_inicio - min_fim);
   
   
   
   
   
   
   
    if (hora_inicio < hora_fim){
        total_horas = hora_fim - hora_inicio -1;
        printf("O JOGO DUROU %i HORA(S) E %i MINUTO(S)\n", total_horas, total_min);
    }
    else if (hora_inicio== hora_fim && min_inicio < min_fim)
        printf("O JOGO DUROU 0 HORA(S) E %i MINUTO(S)\n", total_min);
    else if(hora_inicio > hora_fim){
        total_horas = 24 - (hora_inicio - hora_fim);
        printf("O JOGO DUROU %i HORA(S) E %i MINUTO(S)\n", total_horas, total_min);
    }
    return 0;
}