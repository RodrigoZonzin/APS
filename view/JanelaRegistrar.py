from tkinter import *
from control import controlUser as ct
from . import JanelaLogin as jl

controladorUsuario = ct.UsuarioController()


class JanelaReg:
    def __init__(self, princ, callbackLogin):
        self.princ = princ
        self.root = Toplevel(princ)
        self.root.title('Fazer Cadastro')
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

        #BOTÃO DE LOGIN
        bLogin = Button(
            cabecalho, 
            text='Login', 
            command=lambda: (self.root.destroy(), jl.JanelaLogin(princ, callbackLogin)),
            bg='#546353',
            font=('Verdana', '12')
        )
        bLogin.pack(side='right')

        #BOTÃOI DE VOLTAR
        bVoltar = Button(
            cabecalho, 
            text='Voltar', 
            command=lambda: (self.root.destroy(), princ.deiconify()),
            bg='#546353',
            font=('Verdana', '12')
        )
        bVoltar.pack(side='left')


        #CAMPOS DE DADOS PARA O REGISTRO    
        campoInput = Frame(self.root, bg="#6cbd74") #talvez seja legal mudar a cor desse frame, para dar mais "volume" a tela
        campoInput.pack(pady=70)

        lTitulo = Label(
            campoInput, 
            text='Fazer Cadastro',
            bg='#6cbd74',
            font=('Arial', '20')
        )
        lTitulo.pack(pady=6)

        lNome = Label(
            campoInput, 
            text='Nome',
            bg='#6cbd74',
            font=('Arial', '13')
        )
        lNome.pack(pady=6)
        self.nome = Entry(campoInput)
        self.nome.pack()
       
        lLogin = Label(
            campoInput, 
            text='Login',
            bg='#6cbd74',
            font=('Arial', '13')
        )
        lLogin.pack(pady=6)
        self.login = Entry(campoInput)
        self.login.pack()
       
        lSenha = Label(
            campoInput, 
            text='Senha',
            bg='#6cbd74',
            font=('Arial', '13')    
        )
        lSenha.pack(pady=6)
        self.senha = Entry(campoInput)
        self.senha.pack()

        bEnviar = Button(
            campoInput, 
            text='Enviar', 
            command=self.enviarUsuario,
            font=('Arial', '13')  
        )
        bEnviar.pack(pady=16)

        self.root.mainloop()

    def enviarUsuario(self):
        controladorUsuario.adicionar_usuario(self.nome.get(), self.login.get(), self.senha.get())
        self.princ.deiconify()
        self.root.destroy()


    def fecharPrograma(self):
        #To destruindo essa janela e a janela principal (self.princ) que estava escondida/invisível
        self.root.destroy()
        self.princ.destroy()