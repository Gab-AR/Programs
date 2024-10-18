#include <stdio.h>
int main(){
    typedef struct {
        float x;
        float y;
    } coordenada;
    coordenada c1;
    do{
    scanf("%f%f", &c1.x, &c1.y);
    if (c1.x>0 && c1.y>0)
        printf("Q1\n");
    else if (c1.x<0 && c1.y>0)
        printf ("Q2\n");
    else if (c1.x<0 && c1.y<0)
        printf ("Q3\n");
    else if (c1.x>0 && c1.y<0)
        printf ("Q4\n");
    else if (c1.x==0 && c1.y != 0)
        printf("Eixo y\n");
    else if (c1.y==0 && c1.x != 0)
        printf("Eixo x\n");
    }while(c1.x != 0 || c1.y != 0);
    printf ("Origem\n");
    
    return 0;
}