#import tkinter as tkk
from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
# from control import controle as ct
from . import JanelaLogin as jl
from . import JanelaRegistrar as jr
from . import JanelaBuscar as jb
from . import JanelaUsuarioNormal as ju
from . import JanelaUsuarioAdm as jua
from . import JanelaAtracao as ja
from control.controlLocalTuristico import LocalTuristicoController as lt

# controladorLocalTuristico = ct.LocalTuristicoController()
# controladorUsuario = ct.UsuarioController()

controlLt = lt()

class Janela:
    def __init__(self): 
        self.root = Tk()
        self.root.bind("<Map>", self.atualizaLocais)
        self.isLogged = False
        self.user = StringVar()
        self.userClass = None

        self.locaisAtr = controlLt.retornaTodosLocaisEAtr()

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
            command=self.chamarTelaRegistro,
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
            lNome = Label(self.fr1, text=f'{self.user.get()}', bg='#316b2d')
            lNome.pack(side='left')'''
        
        self.lNome = Label(self.fr1, text='', bg='#316b2d')
        self.lNome.pack(side='left')


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
            command=lambda: (jb.JanelaBuscarLocal(self.barraPesquisa.get()))
        ).pack(side='right', padx=5)

        #BOTÕES DE ALTERAR A TABELA DE LOCAIS/ATRAÇÕES
        # self.fButtun = Frame(self.root).pack(side='top')
        # Button(self.fButtun, text='Registar Local', command=self.chamarInsercaoTL).pack(side='top')
        # Button(self.fButtun, text='Deletar Local', command=jd.JanelaDeletarLocal).pack(side='top')

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

        for i, row in enumerate(self.locaisAtr): 
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
            self.botaoAtracoes.append(Button(self.campoAtracoes[i], bg='white', text=f'Conheça {row[2]}', command = lambda atrc=row :self.chamarTelaAtracoes(atrc)))
            self.botaoAtracoes[i].pack(side='top')

            #breve descrição da atracao turistica
            self.txtAtracoes.append(Label(self.campoAtracoes[i], wraplength=200, width=50, text=f"{row[3]}", bg="yellow"))
            self.txtAtracoes[i].pack()  


        #scroll_bar.config(command=self.frameListagemAtracoes.yview)
        #self.frameListagemAtracoes.config(yscrollcommand=scroll_bar.set)
        self.root.mainloop()

    def chamarTelaLogin(self):
        self.root.withdraw()
        self.root.bind("<Map>", self.atualizaLocais)
        self.janelaLog = jl.JanelaLogin(self.root, self.callbackLogin)

    def chamarTelaRegistro(self):
        self.root.withdraw() 
        self.root.bind("<Map>", self.atualizaLocais)
        jr.JanelaReg(self.root, self.callbackLogin)

    def callbackLogin(self, user):
        self.userClass = user#n sei vamos ver

        self.user.set(user.nome)#n sei vamos ver
        self.isLogged = True
        self.isAdmin = user.isAdmin

        self.lNome.config(text=str(user.nome))
        self.botaoLogin.config(text='Logout', command=self.logOut)
        self.botaoReg.config(text='Usuário', command=self.chamarTelaUser)

    def logOut(self):
        alert = Toplevel(self.root, bg="#6cbd74")
        alert.title('Alerta Logout')
        alert.geometry('315x120')

        fAlert = Frame(alert, bg="#6cbd74")
        fAlert.pack(pady=40)
        
        lAlert = Label(fAlert, text='Logout realizado com sucesso', bg="#6cbd74")
        lAlert.pack()

        self.isLogged = False
        self.user.set('')
        self.lNome.config(text='')
        self.botaoLogin.config(text='Login', command=self.chamarTelaLogin)
        self.botaoReg.config(text='Registrar', command=lambda: (self.root.withdraw(), jr.JanelaReg(self.root, self.callbackLogin)))

    def chamarTelaUser(self):
        self.root.withdraw()
        self.root.bind("<Map>", self.atualizaLocais)
        if self.isAdmin:
            jua.JanelaUsuarioAdm(self.root, self.userClass)
        else:
            ju.JanelaUsuarioNormal(self.root, self.userClass)
        #print('Fazer tela user')

    def chamarTelaAtracoes(self, atrc): 
        self.root.withdraw()
        self.root.bind("<Map>", self.atualizaLocais)
        self.janelaLog = ja.JanelaAtracao(self.root, self.userClass, atrc)

    def destruirTabela(self):
        for i in range(len(self.Atracaoes)):
            self.Atracaoes[i].destroy()
            # self.ReferenciaImgAtracoes[i].destroy() 
            self.imgAtracoes[i].destroy()
            self.campoAtracoes[i].destroy()
            self.botaoAtracoes[i].destroy()
            self.txtAtracoes[i].destroy()

        self.Atracaoes = []
        self.ReferenciaImgAtracoes = [] 
        self.imgAtracoes = []
        self.campoAtracoes = []
        self.botaoAtracoes = []
        self.txtAtracoes = []
            

    def atualizaLocais(self, event): #Essa função vai atualizar o atributo q armazena locais e atracoes. Isso ocorre quando a janela voltar a aparecer.
        #atualizar o atributo de locais e atracoes
        self.locaisAtr = controlLt.retornaTodosLocaisEAtr()

        #destruir a tabela atual
        self.destruirTabela()

        #recriar a tabela de novo
        for i, row in enumerate(self.locaisAtr): 
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
            self.botaoAtracoes.append(Button(self.campoAtracoes[i], bg='white', text=f'Conheça {row[2]}', command = lambda atrc=row :self.chamarTelaAtracoes(atrc)))
            self.botaoAtracoes[i].pack(side='top')

            #breve descrição da atracao turistica
            self.txtAtracoes.append(Label(self.campoAtracoes[i], wraplength=200, width=50, text=f"{row[3]}", bg="yellow"))
            self.txtAtracoes[i].pack()  

        #desativo o bind para evitar que o evento seja acionado toda hora
        self.root.unbind("<Map>")
