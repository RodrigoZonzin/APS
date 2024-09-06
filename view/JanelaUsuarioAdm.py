from tkinter import *
from . import JanelaInserirLocal as ji
from . import JanelaDeletarLocal as jd

from control.controlUser import UsuarioController
from control.controlAvalicao import AvaliacaoController
from control.controlAtracao import AtracaoTuristicaController
from control.controlLocalTuristico import LocalTuristicoController


controlU = UsuarioController()
controlA = AvaliacaoController()
controlAtr = AtracaoTuristicaController()
controlLt = LocalTuristicoController()


class JanelaUsuarioAdm():
    def __init__(self, princ, user):
        self.princ = princ
        self.user = user
        self.allUsers = controlU.retornaAllUsers()
        self.allLocations = controlLt.retornaTodosLocais()
        self.allAtrac = controlAtr.retornaTodasAtracoes()
        self.tabelaAtiva = -1 # -1=nenhuma, 0=users, 1=avaliações, 2=locais, 3=atrações

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
            command=self.tabelaAvaliacao,
            width=10
        )
        btnAvals.pack(pady=5, side='left')

        btnLocais = Button(
            btnFr,
            text='Locais',
            command=self.tabelaLocal,
            width=10
        )
        btnLocais.pack(pady=5, side='left')

        btnAtracoes = Button(
            btnFr,
            text='Atrações',
            command=self.tabelaAtracao,
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

    def chamarInsercaoTL(self, ltAtr):
        ji.JanelaInserirLocal(self.root, ltAtr)

    def destroiTabela(self):
        if self.tabelaAtiva == 0:
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

        elif self.tabelaAtiva == 1:
            for i in range(len(self.listAvalsFr)):
                vec = [self.listAvalsFr, self.fr1, self.fr2, self.locais, self.nota, self.users, self.btnVer, self.btnApagar]
                
                for j in vec:
                    if j[i] != None:
                        j[i].destroy()

            self.listAvalsFr = []
            self.fr1 = []
            self.fr2 = []
            self.locais = []
            self.dataH = []
            self.comentario = []
            self.nota = []
            self.users = [] 
            self.btnVer = []
            self.btnApagar = []

        elif self.tabelaAtiva == 2:
            self.btnAdd[0].destroy()
            self.btnAdd.pop(0)  
            for i in range(len(self.listFr)):
                self.listFr[i].destroy()
                self.nomes[i].destroy()
                self.btnsExcluir[i].destroy()

            self.listFr = []
            self.nomes = []
            self.btnsExcluir = []

        elif self.tabelaAtiva == 3:
            self.btnAdd[0].destroy()
            self.btnAdd.pop(0)
            for i in range(len(self.listFr)):
                self.listFr[i].destroy()
                self.nomes[i].destroy()
                self.btnsExcluir[i].destroy()

            self.listFr = []
            self.nomes = []
            self.btnsExcluir = []

    def destroiLinhaTabela(self, i, aval=None, user=None): #acho q user n será necessário
        if self.tabelaAtiva == 0:
            vec = [self.listFr, self.nomes, self.logins, self.adms, self.btnsExcluir, self.btnsAdm]
            #Apaga usuario
            for j in vec:
                if j[i] != None:
                    j[i].destroy()
                    j.pop(i)
            
            
            # self.listFr[i].destroy()
            # self.nomes[i].destroy()
            # self.logins[i].destroy()
            # self.adms[i].destroy()
            # self.btnsExcluir[i].destroy()
            # self.btnsAdm[i].destroy()

            # self.listFr.pop(i)
            # self.nomes.pop(i)
            # self.logins.pop(i)
            # self.adms.pop(i)
            # self.btnsExcluir.pop(i)
            # self.btnsAdm.pop(i)
            # print(f'Apagou: {self.nomes[i]}')

        elif self.tabelaAtiva == 1:
            #apaga avaliação no bd
            controlU.apagarAvaliacaoAdm(self.user, aval)

            #apagar no model User- Olhar depois se vai ser necessario


            # controlU.apagarAvaliacao(user, aval)
            self.listAvalsFr[i].destroy()
            self.fr1[i].destroy()
            self.fr2[i].destroy()
            self.locais[i].destroy()
            self.nota[i].destroy()
            self.users[i].destroy() 
            self.btnVer[i].destroy()
            self.btnApagar[i].destroy()

            # self.listAvalsFr.pop(i)
            # self.fr1.pop(i)
            # self.fr2.pop(i)
            # self.locais.pop(i)
            # self.nota.pop(i)
            # self.users.pop(i) 
            # self.btnVer.pop(i)
            # self.btnApagar.pop(i)

            self.listAvalsFr[i] = None
            self.fr1[i] = None
            self.fr2[i] = None
            self.locais[i] = None
            self.nota[i] = None
            self.users[i] = None 
            self.btnVer[i] = None
            self.btnApagar[i] = None

        elif self.tabelaAtiva == 2:
                self.listFr[i].destroy()
                self.nomes[i].destroy()
                self.btnsExcluir[i].destroy()

                self.listFr.pop(i)
                self.nomes.pop(i)
                self.btnsExcluir.pop(i)

        elif self.tabelaAtiva == 3:
            self.listFr[i].destroy()
            self.nomes[i].destroy()
            self.btnsExcluir[i].destroy()

            self.listFr.pop(i)
            self.nomes.pop(i)
            self.btnsExcluir.pop(i)

    def tabelaUsers(self):
        self.destroiTabela()
        self.tabelaAtiva = 0

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
                text=f'{item.nome}'
            ))
            self.nomes[i].pack(side='left', padx=7)

            self.logins.append(Label(
                self.listFr[i],
                bg='gray',
                text=f'{item.login}'
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
                command=lambda i=i, login=item.login:self.chamarApagaUser(i, login),
                width=7
            ))
            self.btnsExcluir[i].pack(side='right')

            self.btnsAdm.append(Button(
                self.listFr[i],
                text='',
                command=lambda login=item.login, i=item.isAdmin, index=i:self.chamarMudarAdm(i, login, index),
                width=7
            ))
            self.btnsAdm[i].pack(side='right')

            if item.isAdmin == 0:
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

    def tabelaAvaliacao(self):
        self.destroiTabela()
        self.tabelaAtiva = 1

        avals = controlA.retornaTodasAvals()

        self.listAvalsFr = []
        self.fr1 = []
        self.fr2 = []
        self.locais = []
        self.dataH = []
        self.comentario = []
        self.nota = []
        self.users = [] 
        self.btnVer = []
        self.btnApagar = []

        for i, aval in enumerate(avals):
            self.listAvalsFr.append(Frame(
                self.frLista,
                bg='gray',
                height=200,
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
                text=aval.LocalAtracao.nome,
                bg='gray',
                font=('Verdana', '12')
            ))
            self.locais[i].pack(side="left", padx=5)

            self.users.append(Label(
                self.fr2[i],
                text=f'user: {aval.Autor.login}',
                bg='gray',
                font=('Verdana', '12')
            ))
            self.users[i].pack(side="left", padx=5)

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
                command=lambda user=aval.Autor, i=i, aval = aval: self.destroiLinhaTabela(i, aval, user)
            ))
            self.btnApagar[i].pack(side="right")


    def tabelaLocal(self):
        self.destroiTabela()
        self.tabelaAtiva = 2

        self.btnAdd = []
        btnAddLT = Button(
            self.frLista, 
            text='Registar Local', 
            command=lambda: self.chamarInsercaoTL(1),
            width=10
        )
        btnAddLT.pack(pady=5)
        self.btnAdd.append(btnAddLT)

        for i, item in enumerate(self.allLocations):
            self.listFr.append(Frame(
                self.frLista,
                bg='gray',
                height=80
            ))
            self.listFr[i].pack(fill='x')

            self.nomes.append(Label(
                self.listFr[i],
                bg='gray',
                text=item[2]
            ))
            self.nomes[i].pack(side='left', padx=7)

            self.btnsExcluir.append(Button(
                self.listFr[i],
                text='Excluir',
                command=lambda i=i, id=item[0]: self.chamarApagaLT(i, id),
                width=7
            ))
            self.btnsExcluir[i].pack(side='right')


    def tabelaAtracao(self):
        self.destroiTabela()
        self.tabelaAtiva = 2

        self.btnAdd = []
        btnAddLT = Button(
            self.frLista, 
            text='Registar Local', 
            command=lambda: self.chamarInsercaoTL(1),
            width=10
        )
        btnAddLT.pack(pady=5)
        self.btnAdd.append(btnAddLT)

        for i, item in enumerate(self.allAtrac):
            self.listFr.append(Frame(
                self.frLista,
                bg='gray',
                height=80
            ))
            self.listFr[i].pack(fill='x')

            self.nomes.append(Label(
                self.listFr[i],
                bg='gray',
                text=item[2]
            ))
            self.nomes[i].pack(side='left', padx=7)

            self.btnsExcluir.append(Button(
                self.listFr[i],
                text='Excluir',
                command=lambda i=i, id=item[0]: self.chamarApagaAtr(i, id),
                width=7
            ))
            self.btnsExcluir[i].pack(side='right')


    def chamarMudarAdm(self, i, login, index):
        if login == self.user.login:
            print("ERROR: Tentando se alterar")
            return
        
        res = controlU.mudarAdm(login, i)

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

        try:
            controlA.apagar_todasAvals_user(login)
            controlU.apagar_usuario(login)
            self.destroiLinhaTabela(i)
        except Exception as e:
            print(f'ERROR: {e}')

    def chamarApagaAtr(self, i, id):
        try:
            controlA.apagar_todasAvals_localAtr(id)
            controlAtr.deletarAtracaoTuristico(id)
            self.destroiLinhaTabela(i) 
        except Exception as e:
            print(f'ERROR: {e}')

    def chamarApagaLT(self, i, id):
        try:
            controlA.apagar_todasAvals_localAtr(id)
            controlLt.deletarLocalTuristico(id)
            self.destroiLinhaTabela(i) 
        except Exception as e:
            print(f'ERROR: {e}')

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
            text=f'Local: {aval.LocalAtracao.nome}',
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
            text=f'Data da Avaliação: {aval.dataHora}',
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

    def voltarJanelaPrin(self):
        self.princ.deiconify()
        self.root.destroy()


    def fecharPrograma(self):
        #To destruindo essa janela e a janela principal (self.princ) que estava escondida/invisível
        self.root.destroy()
        self.princ.destroy()