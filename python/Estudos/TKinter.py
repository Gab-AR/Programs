import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dolar: {cotacao_dolar}
    Euro: {cotacao_euro}
    Bitcoin: {cotacao_btc}'''
    
    texto_cotacoes["text"] = texto

janela = Tk()
#janela.geometry("300x250")
janela.title("Cotação Atual das Moedas")
texto_orientação = Label(janela, text="Clique no botão para obter as cotações atuais")
texto_orientação.grid(column=0, row=0, padx=10, pady=10)
botao = Button(janela, text="Buscar", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)
texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()