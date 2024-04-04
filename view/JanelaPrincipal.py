import tkinter as tkk
from tkinter import *
import random

class Janela:

    def __init__(self, toplevel): 
        
        toplevel.title("Empresa de Turismo")
        toplevel.geometry("900x600")
        toplevel.configure(bg="#6cbd74")



        self.fr1 = Frame(toplevel)
        self.fr1.pack()

        self.botao1 = Button(self.fr1)
        self.botao1['background'] = "#aa8c12"
        self.botao1['font'] = ('Verdana', '12')
        self.botao1.bind("<Button-1>", self.muda_cor)
        self.botao1.pack()
        
    
    def muda_cor(self, toplevel, event):
        toplevel.configure(bg=random(1,15000))


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

