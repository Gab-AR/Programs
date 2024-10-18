def menu():
  print("Menu de opções: ")
  print("1.Opção 1")
  print("2.Opção 2")
  print("3.Opção 3")
  print("4.SAIR")
  opcao = int(input())
  while opcao <1 or opcao >4:
    print("Opção inválida! Tente novamente")
    opcao = int(input("Menu de opções: "))
  return opcao
if __name__ == '__main__':
  valor = menu()
  if valor == 1:
    print("Você escolheu a opção 1, o programa continua")
    menu()
  elif valor == 2:
    print("Você escolheu a opção 2, o programa continua")
    menu()
  elif valor == 3:
    print("Você escolheu a opção 3, o programa continua")
    menu()
  else:
    print("Você escolheu a opção SAIR, encerra o programa")