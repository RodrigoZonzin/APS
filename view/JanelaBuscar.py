from tkinter import *
from control.controlLocalTuristico import *

controleLC = LocalTuristicoController()

class JanelaDeletarLocal():
    def __init__(self, nome):
        self.root = Toplevel()
        self.root.title('Busca')
        self.root.geometry('315x120')
        self.root.configure(bg="#6cbd74")
        
        self.frame1 = Frame(self.root, bg='#6cbd74')
        self.frame1.pack(pady=7)

        l1 = Label(
            self.frame1,
            text='',
            bg='#6cbd74'
        )
        l1.pack()

        self.local = controleLC.procuraLocalPorNome(nome)

        #resolver essa parte, q esta só printando os nomes na tela e n a tabela igual na principal
        if self.local != False:
            l1.config(text=self.local.nome)
        else:
            l1.config(text='Nenhum local foi encontrado')