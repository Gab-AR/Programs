import random

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return f"{self.valor} de {self.naipe}"

    def valor_numerico(self):
        valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                   'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return valores[self.valor]

class Baralho:
    naipes = ['Copas', 'Ouros', 'Espadas', 'Paus']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cartas = [Carta(valor, naipe) for naipe in self.naipes for valor in self.valores]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def puxar_carta(self):
        return self.cartas.pop() if self.cartas else None

class JogoWar:
    def __init__(self):
        self.baralho = Baralho()
        self.baralho.embaralhar()

    def jogar(self):
        while len(self.baralho.cartas) > 1:
            carta_jogador1 = self.baralho.puxar_carta()
            carta_jogador2 = self.baralho.puxar_carta()

            print(f"Jogador 1 puxa: {carta_jogador1}")
            print(f"Jogador 2 puxa: {carta_jogador2}")

            if carta_jogador1.valor_numerico() > carta_jogador2.valor_numerico():
                print("Jogador 1 vence a rodada!\n")
            elif carta_jogador2.valor_numerico() > carta_jogador1.valor_numerico():
                print("Jogador 2 vence a rodada!\n")
            else:
                print("Empate!\n")

# Exemplo de execução do jogo:
jogo = JogoWar()
jogo.jogar()
