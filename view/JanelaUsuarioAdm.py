from tkinter import *
from . import JanelaInserirLocal as ji
from . import JanelaDeletarLocal as jd

from control.controlUser import UsuarioController
from control.controlAvalicao import AvaliacaoController

controlU = UsuarioController()
controlA = AvaliacaoController()

class JanelaUsuarioAdm():
    def __init__(self, princ, user):
        self.princ = princ
        self.user = user
        self.allUsers = controlU.retornaAllUsers()
        self.tabelaAtiva = -1 # -1=nenhuma, 0=users, 1=avaliações

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

        btnAddLT = Button(
            btnFr, 
            text='Registar Local', 
            command=self.chamarInsercaoTL,
            width=10
        )
        btnAddLT.pack(side='left')
        btnRemoveLT = Button(
            btnFr, 
            text='Deletar Local', 
            command=jd.JanelaDeletarLocal,
            width=10
        )
        btnRemoveLT.pack(side='left')

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

    def chamarInsercaoTL(self):
        ji.JanelaInserirLocal(self.root)

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
                self.listAvalsFr[i].destroy()
                self.fr1[i].destroy()
                self.fr2[i].destroy()
                self.locais[i].destroy()
                #self.dataH[i].destroy()
                #self.comentario[i].destroy()
                self.nota[i].destroy()
                self.users[i].destroy() 
                self.btnVer[i].destroy()
                self.btnApagar[i].destroy()

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

    def destroiLinhaTabela(self, i, aval, user):
        if self.tabelaAtiva == 0:
            #Apaga usuario
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

            '''self.dataH.append(Label(
                self.fr1[i],
                text=aval[3],
                bg='gray',
                font=('Verdana', '12')
            ))
            self.dataH[i].pack(side="left", padx=5)'''

            '''self.comentario.append(Label(
                self.fr2[i],
                text=f'Comentário: "{aval[1]}"',
                bg='gray',
                font=('Verdana', '12')
            ))
            self.comentario[i].pack(side="left", padx=5)'''

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

        res = controlU.apagar_usuario(login)

        if res == 200:
            self.destroiLinhaTabela(i, None, None) #colocar os outros paramentros aqui

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