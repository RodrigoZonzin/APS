from tkinter import *
from control.controlUser import UsuarioController as un

control = un()

class JanelaUsuarioNormal():
    def __init__(self, princ, user):
        self.princ = princ
        self.user = user

        self.root = Toplevel(self.princ)
        self.root.title("Janela do Usuário")
        self.root.geometry("900x600")
        self.root.config(bg="#6cbd74")

        self.teste()

        #Essa linha reprograma oq acontece ao destruir a janela (como por ex clicar no botão 'x')
        #Nesse caso, ao clicar vai acontecer unicamente oq tiver na funcao self.fecharPrograma
        self.root.protocol("WM_DELETE_WINDOW", self.fecharPrograma)

        #CABEÇALHO DA TELA 
        cabecalho = Frame(
            self.root,
            bg='#316b2d',
            height=140
        )
        cabecalho.pack(side="top", fill = "x")

        #BOTÃO DE VOLTAR
        self.bVoltar = Button(
            cabecalho, 
            text='Voltar', 
            command=self.voltarJanelaPrin,
            bg='#546353',
            font=('Verdana', '12')
        )
        self.bVoltar.pack(side='left')

        corpo = Frame(
            self.root,
            bg="#6cbd74"   
        )
        corpo.pack(fill='both', expand=True)

        nomeUser = Label(
            corpo,
            text=self.user.nome,
            bg="#6cbd74",
            font=('Verdana', '20')
        )
        nomeUser.pack(pady=10)

        """btnComentario = Button(
            corpo,
            text="Criar aval TESTE",
           command=self.teste 
        )
        btnComentario.pack()"""

        frLista = Frame(
            corpo,
            bg="#6cbd74",
            width=600, #pensar em diminuir isso, ou achar uma forma de centralizar o texto
            height=800
        )
        frLista.pack(pady=15)
        frLista.pack_propagate(False)

        self.listAvalsFr = []
        self.fr1 = []
        self.fr2 = []
        self.locais = []
        self.dataH = []
        self.comentario = []
        self.nota = []
        self.btnVer = []
        self.btnApagar = []

        for i, aval in enumerate(self.user.avals):
            self.listAvalsFr.append(Frame(
                frLista,
                bg='gray',
                height=100,
            ))
            self.listAvalsFr[i].pack(fill="x")

            self.fr1.append(Frame(
                self.listAvalsFr[i],
                bg='gray'
            ))
            self.fr1[i].pack(fill="x")

            self.fr2.append(Frame(
                self.listAvalsFr[i],
                bg='gray'
            ))
            self.fr2[i].pack(fill="x")

            self.locais.append(Label(
                self.fr1[i],
                text='local',
                bg='gray',
                font=('Verdana', '15')
            ))
            self.locais[i].pack(side="left", padx=5)

            self.dataH.append(Label(
                self.fr1[i],
                text=aval.dataHora,
                bg='gray',
                font=('Verdana', '12')
            ))
            self.dataH[i].pack(side="left", padx=5)

            self.comentario.append(Label(
                self.fr2[i],
                text=f'Comentário: "{aval.coment}"',
                bg='gray',
                font=('Verdana', '12')
            ))
            self.comentario[i].pack(side="left", padx=5)

            self.nota.append(Label(
                self.fr2[i],
                text=f"Nota: {aval.nota}",
                bg='gray',
                font=('Verdana', '12')
            ))
            self.nota[i].pack(side="left", padx=5)

            self.btnVer.append(Button(
                self.fr1[i],
                text='Ver mais',
                width=10,
                command=lambda a=aval: self.verMais(a)
            ))
            self.btnVer[i].pack(side="right")

            self.btnApagar.append(Button(
                self.fr2[i],
                text='Apagar',
                width=10,
                command=lambda a=aval, i=i: self.apagarAval(a, i)
            ))
            self.btnApagar[i].pack(side="right")


        self.root.mainloop()


    def voltarJanelaPrin(self):
        self.princ.deiconify()
        self.root.destroy()


    def fecharPrograma(self):
        #To destruindo essa janela e a janela principal (self.princ) que estava escondida/invisível
        self.root.destroy()
        self.princ.destroy()


    def apagarAval(self, aval, i):
        control.apagarAvaliacao(self.user, aval)

        self.listAvalsFr[i].destroy()
        self.fr1[i].destroy()
        self.fr2[i].destroy()
        self.locais[i].destroy()
        self.dataH[i].destroy()
        self.comentario[i].destroy()
        self.nota[i].destroy()
        self.btnVer[i].destroy()
        self.btnApagar[i].destroy()


    #Cria o pop-up mostrando todas as informações da avaliação
    def verMais(self, aval):
        vMais = Toplevel(self.root)
        vMais.title('Ver Avaliação')
        vMais.geometry('500x350')
        vMais.config(bg="#6cbd74")

        fr = Frame(
            vMais,
            bg="#6cbd74"
        )
        fr.pack(pady=15)

        nome = Label(
            fr,
            text=f'Local: {aval.idLocalAtracao} (colocar depois o nome)',
            bg="#6cbd74",
            font=('Verdana', '12')
        )
        nome.pack(pady=7)

        nota = Label(
            fr,
            text=f'Nota: {aval.nota}',
            bg="#6cbd74",
            font=('Verdana', '12')
        )
        nota.pack(pady=7)

        coment = Label(
            fr,
            text=f'Comentário: "{aval.coment}"',
            bg="#6cbd74",
            font=('Verdana', '12')
        )
        coment.pack(pady=7)

        dataHora = Label(
            fr,
            text=f'Data e Hora da avaliação: {aval.dataHora}',
            bg="#6cbd74",
            font=('Verdana', '12')
        )
        dataHora.pack(pady=7)

        btn = Button(
            fr,
            text='Fechar',
            command=vMais.destroy
        )
        btn.pack(pady=7)


    #apagar depois
    def verAvals(self):
        #arrumar isso aqui. Fazer algo para mostrar as avaliacoes
        print(self.user.avals[0].nota)


    def teste(self):
        aval = (0, self.user.login, 10, 0, '10/05', 'aaa')
        self.user = control.fazerAvaliacao(self.user, aval)
        aval = (0, self.user.login, 10, 0, '11/05', 'bbb')
        self.user = control.fazerAvaliacao(self.user, aval)
        self.verAvals()