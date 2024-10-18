import math
valorA= float(input("Qual o valor de A?"))
valorB= float(input("Qual o valor de B?"))
valorC= float(input("Qual o valor de C?"))
delta = valorB**2 -(4* valorA * valorC)
if delta > 0:
    x1= (-valorB + math.sqrt(delta))/(2* valorA)
    x2= (-valorB - math.sqrt(delta))/(2* valorA)
    if x1>x2:
            print("as raízes da equação são",x2,"e",x1)
    else:
            print("as raízes da equação são",x1,"e",x2)
if delta == 0:
    print("a raiz desta equação é",(-valorB + math.sqrt(delta))/(2* valorA))
if delta < 0:
    print("esta equação não possui raízes reais")
