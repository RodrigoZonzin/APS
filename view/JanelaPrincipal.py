import tkinter as tkk
from tkinter import *
from PIL import ImageTk, Image
import random
import pandas as pd
from control import controle as ct

controladorLocalTuristico = ct.LocalTuristicoController()
controladorUsuario = ct.UsuarioController()

from . import JanelaLogin as jl

class Janela:

    def __init__(self): 
        root = tkk.Tk()

        #print(controladorLocalTuristico.buscarLocalTuristicoID(1).nome)

        #CONFIGURAÇÃO DA PÁGINA PRINCIPAL
        root.title("Empresa de Turismo")
        root.geometry("900x600")
        root.configure(bg="#6cbd74")


        #CONTAINER QUE CONTERÁ A BARRA DE PESQUISA E O BOTÃO DE LOGIN
        self.fr1 = Frame(root)
        self.fr1['background'] = "#316b2d"
        self.fr1['height'] = 140
        self.fr1.pack(side="top", fill = "x")
        
        #BOTÃO DE LOGIN
        self.botaoLogin = Button(self.fr1)
        self.botaoLogin['background'] = "#546353"
        self.botaoLogin['font'] = ('Verdana', '12')
        self.botaoLogin['text'] = "Login"
        self.botaoLogin.bind("<Button-1>", self.chama_telaLogin)
        self.botaoLogin.pack(side= 'right')
        

        #BOTÃO VOLTAR
        self.botaoVoltar = Button(self.fr1)
        self.botaoVoltar['background'] = "#546353"
        self.botaoVoltar['font'] = ('Verdana', '12')
        self.botaoVoltar['text'] = "Voltar"
        #self.botaoVoltar.bind("<Button-1>", self.voltar)
        self.botaoVoltar.pack(side = 'left', anchor='center')


        #BARRA DE PESQUISA
        self.barraPesquisa = Entry(self.fr1)
        self.barraPesquisa['background'] = "#ffffff"
        self.barraPesquisa['width'] = 40
        self.barraPesquisa['fg'] = 'black'
        self.barraPesquisa['justify'] = 'center'
        self.barraPesquisa.pack(side='top', pady=10)


        #CONTAINER QUE CONTERÁ A LISTAGEM DE ATRAÇÕES TURISTICAS
        self.frameListagemAtracoes = Frame(root)
        self.frameListagemAtracoes['background'] = "#44404a"
        self.frameListagemAtracoes['width'] = 550
        self.frameListagemAtracoes.pack(side = 'top', fill = "y", pady=30)

        #BARRA DE DESCIDA DA PÁGINA
        #NAO ESTÁ FUNCIONANDO
        scroll_bar = Scrollbar(self.frameListagemAtracoes, orient='vertical', command=self.frameListagemAtracoes.yview) 
        scroll_bar.pack(side= 'right', fill='y')

        self.frameListagemAtracoes.configure(yscrollcommand=scroll_bar.set)
        self.frameListagemAtracoes.bind('<Configure>', lambda e: self.frameListagemAtracoes.configure(scrollregion= self.frameListagemAtracoes.bbox('all')))



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

        self.fButtun = Frame(root)
        Button(self.fButtun, text='Registar Local')

        #scroll_bar.config(command=self.frameListagemAtracoes.yview)
        #self.frameListagemAtracoes.config(yscrollcommand=scroll_bar.set)
        root.mainloop()

    def chama_telaLogin(self, event):
        jl.JanelaLogin()
