from tkinter import *

class JanelaUsuarioAdm():
    def __init__(self, princ, user):
        self.princ = princ
        self.user = user

        self.root = Toplevel(self.princ)
        self.root.title("Janela do Usuário")
        self.root.geometry("900x600")
        self.root.config(bg="#6cbd74")

        #Essa linha reprograma oq acontece ao destruir a janela (como por ex clicar no botão 'x')
        #Nesse caso, ao clicar vai acontecer unicamente oq tiver na funcao self.fecharPrograma
        self.root.protocol("WM_DELETE_WINDOW", self.fecharPrograma)

        #CABEÇALHO DA TELA 
        cabecalho = Frame(
            self.root,
            bg='#316b2d',
            height=140
        )
        cabecalho.pack(side="top", fill = "x")

        #BOTÃO DE VOLTAR
        self.bVoltar = Button(
            cabecalho, 
            text='Voltar', 
            command=self.voltarJanelaPrin,
            bg='#546353',
            font=('Verdana', '12')
        )
        self.bVoltar.pack(side='left')

        corpo = Frame(
            self.root,
            bg="#6cbd74"   
        )
        corpo.pack(fill='both', expand=True)

        nomeUser = Label(
            corpo,
            text=self.user.nome,
            bg="#6cbd74",
            font=('Verdana', '20')
        )
        nomeUser.pack(pady=10)

        btnFr = Frame(
            corpo,
            bg="#6cbd74"
        )
        btnFr.pack()


        btnUser = Button(
            btnFr,
            text='Usuários',
            command='',
            width=10
        )
        btnUser.pack(pady=5, side='left')

        btnAvals = Button(
            btnFr,
            text='Avaliações',
            command='',
            width=10
        )
        btnAvals.pack(pady=5, side='left')

        btnAtracoes = Button(
            btnFr,
            text='Atrações',
            command='',
            width=10
        )
        btnAtracoes.pack(pady=5, side='left')

        btnRotas = Button(
            btnFr,
            text='Rotas',
            command='',
            width=10
        )
        btnRotas.pack(pady=5, side='left')


    def voltarJanelaPrin(self):
        self.princ.deiconify()
        self.root.destroy()


    def fecharPrograma(self):
        #To destruindo essa janela e a janela principal (self.princ) que estava escondida/invisível
        self.root.destroy()
        self.princ.destroy()