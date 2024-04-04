import tkinter as tkk
from tkinter import *
import random

class Janela:

    def __init__(self, toplevel): 
        
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
        self.botaoLogin['foreground'] = "#546353"
        self.botaoLogin['font'] = ('Verdana', '12')
        self.botaoLogin['text'] = "Login"
        self.botaoLogin.bind("<Button-1>", self.muda_cor)
        self.botaoLogin.pack(side="right")
        
        #BARRA DE PESQUISA
        self.barraPesquisa = Entry(self.fr1)
        self.barraPesquisa['background'] = "#ffffff"
        self.barraPesquisa['text'] = "Oii To aqui"
        self.barraPesquisa.pack(side='top', anchor='center')

    def muda_cor(self, event):
        self.botaoLogin['background'] = 'yellow'


root = tkk.Tk()
Janela(root)
root.mainloop()
#
#label = tkk.Label(
#    text="Hello, Matheus",
#    foreground="white",  # Set the text color to white
#    background="black",  # Set the background color to black
#    font='verdana'
#)
#label.pack()

