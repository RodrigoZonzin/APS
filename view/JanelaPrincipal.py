import tkinter as tkk
from tkinter import *
from PIL import ImageTk, Image
import random
import pandas as pd
from control import controle as ct
from . import JanelaLogin as jl
from . import JanelaRegistrar as jr

controladorLocalTuristico = ct.LocalTuristicoController()
controladorUsuario = ct.UsuarioController()


class Janela:

    def __init__(self): 
        self.root = tkk.Tk()

        #CONFIGURAÇÃO DA PÁGINA PRINCIPAL
        self.root.title("Empresa de Turismo")
        self.root.geometry("900x600")
        self.root.configure(bg="#6cbd74")


        #CONTAINER QUE CONTERÁ A BARRA DE PESQUISA E O BOTÃO DE LOGIN
        self.fr1 = Frame(self.root)
        self.fr1['background'] = "#316b2d"
        self.fr1['height'] = 140
        self.fr1.pack(side="top", fill = "x")
        
        #BOTÃO DE REGISRAR
        self.botaoReg = Button(self.fr1, text='Registrar', command=self.chama_telaReg)
        self.botaoReg['background'] = "#546353"
        self.botaoReg['font'] = ('Verdana', '12')
        self.botaoReg.pack(side='right')


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

        Button(self.fr1, text='Buscar', command=self.chamaTelaBusca).pack(side='top')


        #CONTAINER QUE CONTERÁ A LISTAGEM DE ATRAÇÕES TURISTICAS
        self.frameListagemAtracoes = Frame(self.root)
        self.frameListagemAtracoes['background'] = "#44404a"
        self.frameListagemAtracoes['width'] = 550
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

        self.fButtun = Frame(self.root).pack(side='top')
        Button(self.fButtun, text='Registar Local', command=self.insercaoTL).pack(side='top')
        Button(self.fButtun, text='Deletar Local', command=self.deletaTL).pack(side='top')

        #scroll_bar.config(command=self.frameListagemAtracoes.yview)
        #self.frameListagemAtracoes.config(yscrollcommand=scroll_bar.set)
        self.root.mainloop()

    def chama_telaLogin(self, event):
        jl.JanelaLogin()

    def chama_telaReg(self):
        jr.JanelaReg()

    def enviarUsuario(self):
        ct.UsuarioController.adicionar_usuario(self.nome.get(), self.login.get(), self.senha.get())

    def insercaoTL(self):
        self.telaInserc = Toplevel(self.root)
        self.telaInserc.title('Inserir Local Turístico')
        self.telaInserc.geometry('300x250')
        self.telaInserc.configure(bg="#6cbd74")

        frame1 = Frame(self.telaInserc)
        frame1.configure(bg="#6cbd74")
        frame1.pack()

        l1 = Label(frame1, text='ID')
        l1.configure(bg="#6cbd74")
        l1.pack()
        self.idLc = Entry(frame1)
        self.idLc.pack()
        l2 = Label(frame1, text='Nome')
        l2.configure(bg="#6cbd74")
        l2.pack()
        self.nomeLc = Entry(frame1)
        self.nomeLc.pack()
        l3 = Label(frame1, text='Endereço')
        l3.configure(bg="#6cbd74")
        l3.pack()
        self.endLc = Entry(frame1)
        self.endLc.pack()
        l4 = Label(frame1, text='Descrição')
        l4.configure(bg="#6cbd74")
        l4.pack()
        self.descLc = Entry(frame1)
        self.descLc.pack()

        #Usa-se o lambda para dar duas funcoes para o comando do botão
        Button(frame1, text='Enviar', command=lambda: (self.enviarInserirLc(), self.telaInserc.destroy())).pack()

    def deletaTL(self):
        self.telaDel = Toplevel(self.root)
        self.telaDel.title('Apagar Local Turístico')
        self.telaDel.geometry('300x250')
        self.telaDel.configure(bg="#6cbd74")

        frame1 = Frame(self.telaDel)
        frame1.configure(bg="#6cbd74")
        frame1.pack()

        l1 = Label(frame1, text='ID')
        l1.configure(bg="#6cbd74")
        l1.pack()
        self.idDel = Entry(frame1)
        self.idDel.pack()
        
        Button(frame1, text='Enviar', command=self.enviarDeletelc).pack()

    def enviarDeletelc(self):
        control = ct.LocalTuristicoController.apagarLocalTuristico(self.idDel.get())
        if control:
            l1 = Label(self.telaDel, text='Local deletado com sucesso')
            l1.configure(bg="#6cbd74")
            l1.pack()
        else:
            l1 = Label(self.telaDel, text='Nao foi possivel deletar o local')
            l1.configure(bg="#6cbd74")
            l1.pack()


    def enviarInserirLc(self):
        ct.LocalTuristicoController.adicionarLocalTuristico(self.idLc.get(), self.nomeLc.get(), self.endLc.get(), self.descLc.get())


    def chamaTelaBusca(self):
        local = ct.LocalTuristicoController.buscarLocalTuristicoNome(self.barraPesquisa.get())

        if local == None:
            self.telaVazia = Toplevel(self.root)
            self.telaVazia.title('Falha na busca')
            self.telaVazia.geometry('300x85')
            self.telaVazia.configure(bg= '#6cbd74')

            l1 = Label(self.telaVazia, text='O nome pesquisado nao foi encontrado')
            l1.configure(bg= '#6cbd74')
            l1.pack(side='top')
            Button(self.telaVazia, text='Fechar', command=self.telaVazia.destroy).pack(side='top')
        else:
            self.telaBusca = Toplevel(self.root)
            self.telaBusca.title('Resultado da Pesquisa')
            self.telaBusca.geometry('550x450')
            self.telaBusca.configure(bg= '#6cbd74')

            #CONTAINER QUE CONTERÁ O BOTOA DE VOLTAR
            self.barraSuperior = Frame(self.telaBusca)
            self.barraSuperior['background'] = "#316b2d"
            self.barraSuperior['height'] = 140
            self.barraSuperior.pack(side="top", fill = "x")

            #BOTAO VOLTAR 
            #ADD O COMANDO VOLTAR 
            self.botaoVoltar = Button(self.barraSuperior, text= "Volte para a Página Inicial", command=self.telaBusca.destroy)
            self.botaoVoltar.pack(side='left')

            #container com as demais informações 
            self.campoResultado = Frame(self.telaBusca)
            self.campoResultado['bg'] = '#6cbd74'
            self.campoResultado.pack(side='top')
            self.campoResultado.pack()

            #campo add imagem 
            #self.referenciaImagem = ImageTk.PhotoImage(Image.open('view/imgs/img_id4.jpg').resize((300, 200)))
            #self.image = self.referenciaImagem;
            #self.campoImagem = Label(self.campoResultado, image = self.referenciaImagem);  #lembrar de colocar o path correto
            #self.campoImagem.pack(side = 'top', pady = 0)

            #campo titulo
            self.tituloBusca = Label(self.campoResultado)
            self.tituloBusca['text'] = f"{local.nome}" #tratar resultado apropriado
            self.tituloBusca['font'] = ('Verdana', '20')
            self.tituloBusca.configure(bg= '#6cbd74')
            self.tituloBusca.pack(side='top')

            #campo descricao
            self.campoDescricao = Label(self.campoResultado)
            self.campoDescricao['text'] = f"{local.descricao}"
            self.campoDescricao.configure(bg= '#6cbd74')
            self.campoDescricao.pack(side='top')