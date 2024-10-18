Totalsegundos= int(input("Por favor, entre com o número de segundos que deseja converter:"))
a= Totalsegundos//86400
segundosrestantes1= Totalsegundos%86400
b= segundosrestantes1//3600
segundosrestantes2= segundosrestantes1%3600
c= segundosrestantes2//60
d= segundosrestantes2%60

print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")
      
