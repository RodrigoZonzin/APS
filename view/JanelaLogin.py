from tkinter import *
from control import controlUser as ct
from .import JanelaRegistrar as jr

controladorUsuario = ct.UsuarioController()

class JanelaLogin():
    def __init__(self, princ, callback): 
        self.princ = princ
        self.callback = callback

        #CONFIGURAÇÃO DA PÁGINA DE LOGIN
        self.root = Toplevel(princ)
        self.root.title("Fazer Login")
        self.root.geometry('900x600')
        self.root.configure(bg="#6cbd74")

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

        #BOTÃO DE Registrar
        bReg = Button(
            cabecalho, 
            text='Registrar', 
            command=lambda: (self.root.destroy(), jr.JanelaReg(princ)),
            bg='#546353',
            font=('Verdana', '12')
        )
        bReg.pack(side='right')

        #BOTÃOI DE VOLTAR
        self.bVoltar = Button(
            cabecalho, 
            text='Voltar', 
            command=self.voltarJenelaPrin,
            bg='#546353',
            font=('Verdana', '12')
        )
        self.bVoltar.pack(side='left')


        #FRAME QUE CONTERÁ TEXTO "LOGIN", CAMPO DE ENTRADA PARA O USUARIO
        #TEXTO "SENHA", CAMPO DE ENTRADA E BOTOA "ENTRAR"
        campoLogin = Frame(self.root, pady=30, bg='#6cbd74')
        campoLogin.pack(side='top', pady=70)

        lTitulo = Label(
            campoLogin, 
            text='Fazer Login',
            bg='#6cbd74',
            font=('Arial', '20')
        )
        lTitulo.pack(pady=6)

        textoNome = Label(
            campoLogin, 
            text="Usuario:",
            bg='#6cbd74',
            font=('Arial', '13')
        )
        textoNome.pack(side='top', pady=6)

        self.entradaNome = Entry(campoLogin)
        self.entradaNome.pack(side='top')

        textoSenha = Label(
            campoLogin, 
            text="Senha:", 
            bg='#6cbd74',
            font=('Arial', '13')  
        )
        textoSenha.pack(side='top', pady=6)
        
        self.entradaSenha = Entry(campoLogin)
        self.entradaSenha.pack(side='top')

        botaoEntrar = Button(
            campoLogin, 
            text="Entrar", 
            command=self.entrar,
            font=('Arial', '13')  
        )
        botaoEntrar.pack(side='top', pady=16)

        self.labelLogin = Label(
            self.root,
            text='',
            bg='#6cbd74'
        )
        self.labelLogin.pack()

        self.root.mainloop()

    def entrar(self):
        # Obtendo o texto das entradas
        usuario = self.entradaNome.get()
        senha = self.entradaSenha.get()
        
        response = controladorUsuario.fazer_login(usuario, senha) #Como passar essa info a janela principal
        
        if response != None:
            self.labelLogin.configure(text=f'Login feito com sucesso. Seja bem vindo {response.nome}!\nRedirecinando a tela principal.')
            self.user = response

            #faz uma pausa de 2segs antes de executar  oo voltarJanelaPrin
            self.callback(response)
            self.root.after(1500, self.voltarJenelaPrin)
        
        else:
            self.labelLogin.config(text='Login ou senha invalidos')


    def voltarJenelaPrin(self):
        self.princ.deiconify()
        self.root.destroy()

    def fecharPrograma(self):
        #To destruindo essa janela e a janela principal (self.princ) que estava escondida/invisível
        self.root.destroy()
        self.princ.destroy()