import tkinter as tkk
from tkinter import *
from PIL import ImageTk, Image
import random
import pandas as pd

class Janela:

    def __init__(self, toplevel): 
        #CONFIGURAÇÃO DA PÁGINA PRINCIPAL
        toplevel.title("Empresa de Turismo")
        toplevel.geometry("900x600")
        toplevel.configure(bg="#6cbd74")


        #CONTAINER QUE CONTERÁ A BARRA DE PESQUISA E O BOTÃO DE LOGIN
        self.fr1 = Frame(toplevel)
        self.fr1['background'] = "#316b2d"
        self.fr1['height'] = 140
        self.fr1.pack(side="top", fill = "x")
        
        #BOTÃO DE LOGIN
        self.botaoLogin = Button(self.fr1)
        self.botaoLogin['background'] = "#546353"
        self.botaoLogin['font'] = ('Verdana', '12')
        self.botaoLogin['text'] = "Login"
        self.botaoLogin.bind("<Button-1>", self.muda_cor)
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
        self.frameListagemAtracoes = Frame(toplevel)
        self.frameListagemAtracoes['background'] = "#44404a"
        #self.frameListagemAtracoes['height'] = 500
        self.frameListagemAtracoes['width'] = 550
        self.frameListagemAtracoes.pack(side = 'top', fill = "y", pady=30)

        scroll_bar = Scrollbar(self.frameListagemAtracoes) 
        scroll_bar.pack(side= 'right', fill='y')

        infoCidades = pd.read_csv("APS/bancoDeDados/atracaoTuristica.csv", sep=';')
        

        self.Atracaoes = []
        self.ReferenciaImgAtracoes = [] 
        self.imgAtracoes = []
        self.campoAtracoes = []
        self.botaoAtracoes = []
        self.txtAtracoes = []

        for i, row in enumerate(infoCidades.itertuples(index=False)): 
            self.Atracaoes.append(Frame(self.frameListagemAtracoes))
            self.Atracaoes[i]['background'] = "gray"
            self.Atracaoes[i]['height'] = 100
            self.Atracaoes[i].pack(side='top', fill='y')

        self.ReferenciaImgAtracao2 = ImageTk.PhotoImage(Image.open("APS/view/imgs/saopaulo.jpg").resize((200, 100)))
        self.imgAtracao2 = Label(self.Atracao2, image=self.ReferenciaImgAtracao2, width = 200, height=100)
        self.imgAtracao2.image = self.ReferenciaImgAtracao
        self.imgAtracao2.grid(column=0, row = 0)

        
        self.txtAtracao2 = Label(self.Atracao2, wraplength=200)
        self.txtAtracao2['width'] = 50
        self.txtAtracao2['text'] = "A rota turistica de São Paulo permite uma imersão no ambiente cosmopolita da sociedade pós industrial nazicapitalista"
        self.txtAtracao2['bg'] = "yellow"
        self.txtAtracao2.grid(column=1, row = 0)




    def muda_cor(self, event):
        self.botaoLogin['background'] = 'yellow'

root = tkk.Tk()
Janela(root)
root.mainloop()
