#include <stdio.h>

int main() {

double A,B,C,f;
scanf("%lf%lf%lf",&A,&B,&C);

if(C>A){
    f=A;
    A=C;
    C=f;
}
if(B > A){
    f=A;
    A=B;   
    B=f;
}
if(A>=B+C) printf("NAO FORMA TRIANGULO\n");
else{
if(A*A == B*B + C*C) printf("TRIANGULO RETANGULO\n");
if(A*A>B*B+C*C) printf("TRIANGULO OBTUSANGULO\n");
if(A*A<B*B+C*C) printf("TRIANGULO ACUTANGULO\n");
if(A==B&&B==C&& A==C) printf("TRIANGULO EQUILATERO\n");
else {
    if(A==B || A==C || B==C) printf("TRIANGULO ISOSCELES\n");
}
}
return 0;
}