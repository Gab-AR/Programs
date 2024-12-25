from tkinter import *

def criar_janela_pergunta():
    janela = Tk()
    janela.title("Pergunta")
    janela.geometry("300x150")

    pergunta = Label(janela, text="Me faz um pix de 500 pila?", font=("Arial", 12))
    pergunta.pack(pady=20)

    def resposta_nao():
        janela.destroy()
        criar_janela_pergunta()

    def resposta_sim():
        janela.destroy()
        criar_janela_resposta()

    botao_sim = Button(janela, text="Sim", command=resposta_sim, width=10)
    botao_sim.pack(side=LEFT, padx=20, pady=20)

    botao_nao = Button(janela, text="Não", command=resposta_nao, width=10)
    botao_nao.pack(side=RIGHT, padx=20, pady=20)

    janela.mainloop()

def criar_janela_resposta():
    def pix_email():
        chave_pix["text"] = "gabriegael@gmail.com"

    def pix_celular():
        chave_pix["text"] = "86988385498"

    def pix_cpf():
        chave_pix["text"] = "Tá doido que eu vou te dar meu CPF?\nKKKKKKKKKKK\nEscolhe outra chave aí, man."

    janela2 = Tk()
    janela2.title("Resposta")
    janela2.geometry("625x250")  

    resposta = Label(janela2, text="AEEEEEEEEEEEE!!!", font=("Arial", 14), fg="green")
    resposta.pack(padx=10, pady=10)

    resposta2 = Label(janela2, text="Você pode até escolher qual das minhas chaves Pix quer usar, eu tenho 3!", font=("Arial", 12))
    resposta2.pack(padx=10, pady=10)

    frame_botoes = Frame(janela2)
    frame_botoes.pack(pady=10)

    email = Button(frame_botoes, text="Email", command=pix_email, width=10)
    email.pack(side=LEFT, padx=10)

    celular = Button(frame_botoes, text="Celular", command=pix_celular, width=10)
    celular.pack(side=LEFT, padx=10)

    cpf = Button(frame_botoes, text="CPF", command=pix_cpf, width=10)
    cpf.pack(side=LEFT, padx=10)

    chave_pix = Label(janela2, text="", font=("Arial", 12), fg="blue")
    chave_pix.pack(padx=10, pady=20) 

    janela2.mainloop()

criar_janela_pergunta()
