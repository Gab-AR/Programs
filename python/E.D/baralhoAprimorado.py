import random

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
    
    def __repr__(self):
        return f"{self.valor} de {self.naipe}"
    
    def valor_numerico(self):
        valores = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                   'J': 11, 'Q': 12, 'K': 13}
        return valores[self.valor]
    
class Baralho:
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    naipes = ['Ouros', 'Paus', 'Espadas', 'Copas']

    def __init__(self):
        self.cartas = [Carta(valor, naipe) for naipe in self.naipes for valor in self.valores]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def pegarCarta(self):
        return self.cartas.pop() if self.cartas else None
    
    def reiniciar(self):
        self.__init__()
        self.embaralhar()

class Jogar:
    def __init__(self):
        self.baralho = Baralho()
        self.baralho.embaralhar()
        print('')
        print("Bem vindo ao WAR!!")
        print("Cada jogador vai receber uma carta e vence quem tiver a maior.")
        print("Boa sorte!")
        print('')

    def encerrar(self, vitorias1, vitorias2, empates):
        print('')
        print("Obrigado por jogar, até a proxima!")
        print(f'Jogador 1 venceu {vitorias1} partidas.')
        print(f'Jogador 2 venceu {vitorias2} partidas.')
        print(f'Houveram {empates} empates.')

    def comecar(self):
        escolha = 'y'
        rodada = 1
        vitorias1 = 0
        vitorias2 = 0
        empates = 0
        while escolha == 'y':
            carta_jogador1 = self.baralho.pegarCarta()
            carta_jogador2 = self.baralho.pegarCarta()
            print('')
            print(f"Jogador 1 puxa: {carta_jogador1}")
            print(f"Jogador 2 puxa: {carta_jogador2}")
            if carta_jogador1.valor_numerico() > carta_jogador2.valor_numerico():
                print(f'Jogador 1 venceu a rodada {rodada}')
                vitorias1 += 1
            elif carta_jogador2.valor_numerico() > carta_jogador1.valor_numerico():
                print(f'Jogador 2 vendeu a rodada {rodada}')
                vitorias2 += 1
            else:
                print(f'Empate na rodada {rodada}')
                empates += 1
            rodada += 1
            escolha = ''
            if len(self.baralho.cartas) > 1:
                while escolha != 'y' and escolha != 'n':
                    print('')
                    escolha = input("Quer jogar outra rodada? y-sim n-nao\n").lower()
                    if escolha == 'n':
                        self.encerrar(vitorias1, vitorias2, empates)
                        return
            else:
                denovo = ''
                while denovo != 'y' and denovo != 'n':
                    print('')
                    denovo = input("Cartas insuficientes, deseja pegar outro baralho? y-sim n-nao\n").lower()
                    if denovo == 'n':
                        self.encerrar(vitorias1, vitorias2, empates)
                        return 
                    if denovo == 'y':
                        escolha = 'y'
                        self.baralho.reiniciar()
                        print('')
                        print("Cartas reestabelecidas, comecando proxima partida.")
                        print('')
                        break

jogo = Jogar()
jogo.comecar()