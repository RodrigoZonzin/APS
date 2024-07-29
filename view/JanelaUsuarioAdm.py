from tkinter import *

from control.controlUser import UsuarioController

control = UsuarioController()

class JanelaUsuarioAdm():
    def __init__(self, princ, user):
        self.princ = princ
        self.user = user
        self.allUsers = control.retornaAllUsers()

        self.root = Toplevel(self.princ)
        self.root.title("Janela do Usuário")
        self.root.geometry("900x600")
        self.root.config(bg="#6cbd74")

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

        btnFr = Frame(
            corpo,
            bg="#6cbd74"
        )
        btnFr.pack()


        btnUser = Button(
            btnFr,
            text='Usuários',
            command=self.tabelaUsers,
            width=10
        )
        btnUser.pack(pady=5, side='left')

        btnAvals = Button(
            btnFr,
            text='Avaliações',
            command=self.destroiTabela, #teste
            width=10
        )
        btnAvals.pack(pady=5, side='left')

        btnAtracoes = Button(
            btnFr,
            text='Atrações',
            command='',
            width=10
        )
        btnAtracoes.pack(pady=5, side='left')

        btnRotas = Button(
            btnFr,
            text='Rotas',
            command='',
            width=10
        )
        btnRotas.pack(pady=5, side='left')

        self.frLista = Frame(
            corpo,
            bg="#6cbd74",
            width=400, #pensar em diminuir isso, ou achar uma forma de centralizar o texto
            height=800
        )
        self.frLista.pack(pady=15)
        self.frLista.pack_propagate(False)

        self.listFr = []
        self.nomes = []
        self.logins = []
        self.adms = []
        self.btnsExcluir = []
        self.btnsAdm = []

        self.tabelaUsers()


    def destroiTabela(self):
        for i in range(len(self.listFr)):
            self.listFr[i].destroy()
            self.nomes[i].destroy()
            self.logins[i].destroy()
            self.adms[i].destroy()
            self.btnsExcluir[i].destroy()
            self.btnsAdm[i].destroy()

        self.listFr = []
        self.nomes = []
        self.logins = []
        self.adms = []
        self.btnsExcluir = []
        self.btnsAdm = []

    def destroiLinhaTabela(self, i):
        self.listFr[i].destroy()
        self.nomes[i].destroy()
        self.logins[i].destroy()
        self.adms[i].destroy()
        self.btnsExcluir[i].destroy()
        self.btnsAdm[i].destroy()

        self.listFr.pop(i)
        self.nomes.pop(i)
        self.logins.pop(i)
        self.adms.pop(i)
        self.btnsExcluir.pop(i)
        self.btnsAdm.pop(i)

    def tabelaUsers(self):
        self.destroiTabela()

        for i, item in enumerate(self.allUsers):
            self.listFr.append(Frame(
                self.frLista,
                bg='gray',
                height=80
            ))
            self.listFr[i].pack(fill='x')

            self.nomes.append(Label(
                self.listFr[i],
                bg='gray',
                text=f'{item[1]}'
            ))
            self.nomes[i].pack(side='left', padx=7)

            self.logins.append(Label(
                self.listFr[i],
                bg='gray',
                text=f'{item[2]}'
            ))
            self.logins[i].pack(side='left', padx=7)

            self.adms.append(Label(
                self.listFr[i],
                bg='gray',
                text=f''
            ))
            self.adms[i].pack(side='left', padx=7)

            self.btnsExcluir.append(Button(
                self.listFr[i],
                text='Excluir',
                command=lambda i=i, login=item[2]:self.chamarApagaUser(i, login),
                width=7
            ))
            self.btnsExcluir[i].pack(side='right')

            self.btnsAdm.append(Button(
                self.listFr[i],
                text='',
                command=lambda login=item[2], i=item[4], index=i:self.chamarMudarAdm(i, login, index),
                width=7
            ))
            self.btnsAdm[i].pack(side='right')

            if item[4] == 0:
                self.adms[i].configure(
                    text='É adm? Não'
                )

                self.btnsAdm[i].configure(
                    text='Tornar Adm',
                )

            else:
                self.adms[i].configure(
                    text='É adm? Sim'
                )

                self.btnsAdm[i].configure(
                    text='Tirar Adm',
                )

    def chamarMudarAdm(self, i, login, index):
        if login == self.user.login:
            print("ERROR: Tentando se alterar")
            return
        
        res = control.mudarAdm(login, i)

        if res == 200:
            if i == 0:
                self.btnsAdm[index].configure(text='Tirar Adm')
                self.adms[index].configure(text='É adm? Sim')
            else:
                self.btnsAdm[index].configure(text='Tornar Adm')
                self.adms[index].configure(text='É adm? Não')

    def chamarApagaUser(self, i, login):
        if login == self.user.login:
            print("ERROR: Tentando se apagar")
            return

        res = control.apagar_usuario(login)

        if res == 200:
            self.destroiLinhaTabela(i)

    def voltarJanelaPrin(self):
        self.princ.deiconify()
        self.root.destroy()


    def fecharPrograma(self):
        #To destruindo essa janela e a janela principal (self.princ) que estava escondida/invisível
        self.root.destroy()
        self.princ.destroy()