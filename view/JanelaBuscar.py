from tkinter import *
from control.controlLocalTuristico import *
from model.LocalTuristico import *

controleLC = LocalTuristicoController()

class JanelaBuscarLocal():
    def __init__(self, nome):
        #print(f"LUGAR BUSCA {nome}")
        self.root = Toplevel()
        self.root.title('Busca')
        self.root.geometry("900x600")
        self.root.configure(bg="#6cbd74")
        
        self.frame1 = Frame(self.root, bg='#6cbd74')
        self.frame1.pack(pady=7)

        #REALZIA A PESQUISA NO BANCO DE DADOS
        self.atributos = controleLC.procuraLocalPorNome(nome) #id, is_LTAtr, nome, endereco, descricao
        print(self.atributos)
        
        if self.atributos != False:
            self.objeto_local = LocalTuristico(self.atributos[0], self.atributos[2], self.atributos[3], self.atributos[4])

            self.frame_tabela = Frame(
                self.frame1,
                bg=  '#6cbd74'
                )
            self.frame_tabela.pack(side = 'top', fill = 'x', pady = 50)
                        
            self.titulo = Label(
                self.frame_tabela,
                bg = '#6cbd74',
                text = self.objeto_local.nome
            )
            self.titulo.grid(row = 0, column = 0)

            self.descricaoLocal = Label(
                self.frame_tabela,
                bg = '#6cbd74',
                text = self.objeto_local.descricao
            )
            self.descricaoLocal.grid(row = 1, column = 0)

        else:
            self.mensagemErro = Label(
                self.frame1,
                bg = '#6cbd74',
                text = 'Local não encontrado. Tente novamente!'
            )
            self.mensagemErro.pack(side = 'top')