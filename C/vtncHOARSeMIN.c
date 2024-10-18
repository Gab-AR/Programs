#include <stdio.h>
int main(){
	int hora_inicio,min_inicio,hora_fim,min_fim;
    scanf("%i %i %i %i", &hora_inicio, &min_inicio, &hora_fim, &min_fim);
	
	int tempo_inicio,tempo_fim,variacao,variacao_hora,variacao_min;
	tempo_inicio = (hora_inicio * 60) + min_inicio;
	tempo_fim = (hora_fim * 60) + min_fim;
	
	if (tempo_fim <= tempo_inicio)
	tempo_fim = tempo_fim + (24*60);
	
	variacao = tempo_fim - tempo_inicio;
	variacao_hora = variacao / 60;
	variacao_min = variacao % 60;
	
	printf("O JOGO DUROU %i HORA(S) E %i MINUTO(S)\n",variacao_hora,variacao_min);
	return 0;
}