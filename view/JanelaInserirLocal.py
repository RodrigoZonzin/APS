from tkinter import *
from control.controlLocalTuristico import *

controleLC = LocalTuristicoController()

class JanelaInserirLocal():
    def __init__(self, princ):
        self.root = Toplevel()
        self.root.title('Inserir Local Turístico')
        self.root.geometry('315x250')
        self.root.configure(bg="#6cbd74")

        self.frame1 = Frame(self.root, bg="#6cbd74")
        self.frame1.pack()

        l1 = Label(
            self.frame1, 
            text='ID',
            bg="#6cbd74"    
        )
        l1.pack()
        self.idLc = Entry(self.frame1)
        self.idLc.pack()
        
        l2 = Label(
            self.frame1, 
            text='Nome',
            bg="#6cbd74"
        )
        l2.pack()
        self.nomeLc = Entry(self.frame1)
        self.nomeLc.pack()
        
        l3 = Label(
            self.frame1, 
            text='Endereço',
            bg="#6cbd74"
        )
        l3.pack()
        self.endLc = Entry(self.frame1)
        self.endLc.pack()
        
        l4 = Label(
            self.frame1, 
            text='Descrição',
            bg="#6cbd74"
        )
        l4.pack()
        self.descLc = Entry(self.frame1)
        self.descLc.pack()

        #Usa-se o lambda para dar duas funcoes para o comando do botão
        b1 = Button(
            self.frame1, 
            text='Enviar', 
            command=self.enviarLocalT
        )
        b1.pack()

        #Label q vai ser usado na enviarLocalLT
        self.lresp = Label(
            self.frame1,
            text='',
            bg='#6cbd74'    
        )
        self.lresp.pack()


    def enviarLocalT(self):
        if self.idLc.get() == '' or self.nomeLc.get() == '' or self.endLc.get() == '' or self.descLc.get() == '':
            #Não inseriu nada
            self.lresp.config(text='Por favor insira todas as infromações')
        else:
            response = controleLC.adicionarLocalTuristico(self.idLc.get(), self.nomeLc.get(), self.endLc.get(), self.descLc.get())

            if response != None:
                self.lresp.config(text='Local Turistico Adicionado com sucesso!')

            else:
                self.lresp.config(text='Ocorreu um erro inesperado ao adicionar o Local Turistico')
