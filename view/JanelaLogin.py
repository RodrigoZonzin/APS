import tkinter as tkk
from tkinter import *
from PIL import ImageTk, Image
import random
import pandas as pd


class JanelaLogin():

    def __init__(self): 
        #CONFIGURAÇÃO DA PÁGINA DE LOGIN
        
        self.janelaLogin = Toplevel()
        self.janelaLogin.title("Página de Login")
        self.janelaLogin.geometry('300x250')
        self.janelaLogin.configure(bg="#6cbd74")


        #CONTAINER QUE CONTERÁ O BOTOA DE VOLTAR
        self.barraSuperior = Frame(self.janelaLogin)
        self.barraSuperior['background'] = "#316b2d"
        self.barraSuperior['height'] = 140
        self.barraSuperior.pack(side="top", fill = "x")

        self.botaoVoltar = Button(self.barraSuperior, text= "Volte para a Página Inicial", command=self.janelaLogin.destroy)
        self.botaoVoltar.pack(side='left')

        #FRAME QUE CONTERÁ TEXTO "LOGIN", CAMPO DE ENTRADA PARA O USUARIO
        #TEXTO "SENHA", CAMPO DE ENTRADA E BOTOA "ENTRAR"
        self.campoLogin = Frame(self.janelaLogin, pady=30)
        self.campoLogin.configure(bg="#6cbd74")
        self.campoLogin.pack(side='top')

        self.textoNome = Label(self.campoLogin, text="Usuario:")
        self.textoNome.configure(bg="#6cbd74")
        self.textoNome.pack(side='top')

        self.entradaNome = Entry(self.campoLogin)
        self.entradaNome.pack(side='top')

        self.textoSenha = Label(self.campoLogin, text="Senha:", pady=10)
        self.textoSenha.configure(bg="#6cbd74")
        self.textoSenha.pack(side='top')
        
        self.entradaSenha = Entry(self.campoLogin)
        self.entradaSenha.pack(side='top')

        self.botaoEntrar = Button(self.campoLogin, text="Entrar", command=self.entrar)
        self.botaoEntrar.pack(side='top')


    def entrar(self):
        # Obtendo o texto das entradas
        usuario = self.entradaNome.get()
        senha = self.entradaSenha.get()
        
        # Exibindo o texto para demonstração
        print("Usuário:", usuario)
        print("Senha:", senha)
