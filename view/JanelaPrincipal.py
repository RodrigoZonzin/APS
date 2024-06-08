import tkinter as tkk
from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
from control import controle as ct
from . import JanelaLogin as jl
from . import JanelaRegistrar as jr
from . import JanelaInserirLocal as ji
from . import JanelaDeletarLocal as jd
from . import JanelaBuscar as jb

controladorLocalTuristico = ct.LocalTuristicoController()
controladorUsuario = ct.UsuarioController()


class Janela:
    def __init__(self): 
        self.isLogged = True
        #self.user = StringVar()
        #self.user.set('abc')
        self.root = Tk()

        #CONFIGURAÇÃO DA PÁGINA PRINCIPAL
        self.root.title("Empresa de Turismo")
        self.root.geometry("900x600")
        self.root.configure(bg="#6cbd74")


        #CONTAINER QUE CONTERÁ A BARRA DE PESQUISA E O BOTÃO DE LOGIN
        self.fr1 = Frame(
            self.root,
            bg='#316b2d',
            height=140
        )
        self.fr1.pack(side="top", fill = "x")
        
        #BOTÃO DE REGISRAR
        self.botaoReg = Button(
            self.fr1, 
            text='Registrar', 
            command=lambda: (self.root.withdraw(), jr.JanelaReg(self.root)),
            bg='#546353',
            font=('Verdana', '12')
        )
        self.botaoReg.pack(side='left')

        #BOTÃO DE LOGIN
        self.botaoLogin = Button(
            self.fr1,
            text='Login',
            bg='#546353',
            font=('Verdana', '12'),
            command=self.chamarTelaLogin
        )
        self.botaoLogin.pack(side= 'right')        

        #APENAS TESTE
        '''if self.isLogged:
            lTeste = Label(self.fr1, text=f'{self.user}', bg='#316b2d')
            lTeste.pack(side='left')'''


        #BOTÃO VOLTAR
        '''self.botaoVoltar = Button(self.fr1)
        self.botaoVoltar['background'] = "#546353"
        self.botaoVoltar['font'] = ('Verdana', '12')
        self.botaoVoltar['text'] = "Voltar"
        #self.botaoVoltar.bind("<Button-1>", self.voltar)
        self.botaoVoltar.pack(side = 'left', anchor='center')'''

        #FRAME PESQUISA
        self.fr2 = Frame(self.fr1, bg='#316b2d')
        self.fr2.pack()

        #BARRA DE PESQUISA
        self.barraPesquisa = Entry(
            self.fr2,
            bg='#ffffff',
            width=40,
            fg='black',
            justify='center'
        )
        self.barraPesquisa.pack(side='left', pady=10, padx=5)

        Button(
            self.fr2, 
            text='Buscar', 
            command=lambda: (jb.JanelaDeletarLocal(self.barraPesquisa.get()))
        ).pack(side='right', padx=5)

        #BOTÕES DE ALTERAR A TABELA DE LOCAIS/ATRAÇÕES
        self.fButtun = Frame(self.root).pack(side='top')
        Button(self.fButtun, text='Registar Local', command=self.chamarInsercaoTL).pack(side='top')
        Button(self.fButtun, text='Deletar Local', command=jd.JanelaDeletarLocal).pack(side='top')

        #CONTAINER QUE CONTERÁ A LISTAGEM DE ATRAÇÕES TURISTICAS
        self.frameListagemAtracoes = Frame(
            self.root,
            bg='#44404a',
            width=550
        )
        self.frameListagemAtracoes.pack(side = 'top', fill = "y", pady=30)

        #BARRA DE DESCIDA DA PÁGINA
        #NAO ESTÁ FUNCIONANDO
        #scroll_bar = Scrollbar(self.frameListagemAtracoes, orient='vertical', command=self.frameListagemAtracoes.yview) 
        #scroll_bar.pack(side= 'right', fill='y')

        #self.frameListagemAtracoes.configure(yscrollcommand=scroll_bar.set)
        #self.frameListagemAtracoes.bind('<Configure>', lambda e: self.frameListagemAtracoes.configure(scrollregion= self.frameListagemAtracoes.bbox('all')))



        #infoCidades = pd.read_csv("APS/bancoDeDados/atracaoTuristica.csv", sep=';')
        infoCidades = pd.read_json('./banco.json');
        

        self.Atracaoes = []
        self.ReferenciaImgAtracoes = [] 
        self.imgAtracoes = []
        self.campoAtracoes = []
        self.botaoAtracoes = []
        self.txtAtracoes = []

        for i, row in enumerate(infoCidades.itertuples()): 
            self.Atracaoes.append(Frame(self.frameListagemAtracoes, pady=10))
            self.Atracaoes[i]['background'] = "gray"
            self.Atracaoes[i]['height'] = 100
            self.Atracaoes[i].pack(side='top', fill='y')

            #imagem da atração
            self.ReferenciaImgAtracoes.append(ImageTk.PhotoImage(Image.open("./view/imgs/img_id1.jpg").resize((200, 100))))
            self.imgAtracoes.append(Label(self.Atracaoes[i], image=self.ReferenciaImgAtracoes[i], width=200, height=100))
            self.imgAtracoes[i].image = self.ReferenciaImgAtracoes[i]
            self.imgAtracoes[i].grid(column=0, row=0)

            #container para adicionar o botao e o texto, ao lado da imagem
            self.campoAtracoes.append(Frame(self.Atracaoes[i]))
            self.campoAtracoes[i].grid(column=1, row=0)

            #botao 'conheca tal lugar' para redirecionar a pagina
            self.botaoAtracoes.append(Button(self.campoAtracoes[i], bg='white', text=f'Conheça {row.Nome}'))
            self.botaoAtracoes[i].pack(side='top')

            #breve descrição da atracao turistica
            self.txtAtracoes.append(Label(self.campoAtracoes[i], wraplength=200, width=50, text=f"{row.Descricao}", bg="yellow"))
            self.txtAtracoes[i].pack()  


        #scroll_bar.config(command=self.frameListagemAtracoes.yview)
        #self.frameListagemAtracoes.config(yscrollcommand=scroll_bar.set)
        self.root.mainloop()

    def chamarTelaLogin(self):
        self.root.withdraw()
        self.janelaLog = jl.JanelaLogin(self.root, self.callbackLogin)

    def callbackLogin(self, user):
        self.user.set(user.nome)
        self.isLogged = True

    def chamarInsercaoTL(self):
        ji.JanelaInserirLocal(self.root)