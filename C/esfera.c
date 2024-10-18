#include <stdio.h>
#include <math.h>
int main (){
    double raio, PI = 3.14159, volume;
    scanf("%lf", &raio);
    volume = (4.0/3.0)* PI * pow(raio, 3);
    printf("VOLUME = %.3lf\n", volume);
    return 0;
}