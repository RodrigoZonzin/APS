from tkinter import *
from control.controlLocalTuristico import *

controleLC = LocalTuristicoController()

class JanelaDeletarLocal():
    def __init__(self):
        self.root = Toplevel()
        self.root.title('Deletar Local Turístico')
        self.root.geometry('315x120')
        self.root.configure(bg="#6cbd74")

        self.frame1 = Frame(self.root, bg="#6cbd74")
        self.frame1.pack(pady=7)

        l1 = Label(
            self.frame1, 
            text='ID',
            bg="#6cbd74"    
        )
        l1.pack()
        self.idLc = Entry(self.frame1)
        self.idLc.pack()

        bEnviar = Button(
            self.frame1,
            text='Enviar',
            command=self.deletarLocalT
        )
        bEnviar.pack(pady=5)

        #Label q vai ser usado no deletarLocalLT
        self.lresp = Label(
            self.frame1,
            text='',
            bg='#6cbd74'    
        )
        self.lresp.pack()

    def deletarLocalT(self):
        if self.idLc.get() == '':
            #Não inseriu nada
            self.lresp.config(text='Por favor insira o id do local')
        else:
            response = controleLC.deletarLocalTuristico(self.idLc.get())

            if response:
                self.lresp.config(text='Local Turistico deletado com sucesso!')

            else:
                self.lresp.config(text='Ocorreu um erro inesperado ao adicionar o Local Turistico') 