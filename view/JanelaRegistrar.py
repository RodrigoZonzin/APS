from tkinter import *

class JanelaReg:
    def __init__(self):
        self.root = Tk()
        self.root.title('Fazer Cadastro')
        self.root.geometry('900x600')
        self.root.configure(bg="#6cbd74")

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
            command='',
            bg='#546353',
            font=('Verdana', '12')
        )
        bLogin.pack(side='right')

        #BOTÃOI DE VOLTAR
        bVoltar = Button(
            cabecalho, 
            text='Voltar', 
            command='',
            bg='#546353',
            font=('Verdana', '12')
        )
        bVoltar.pack(side='left')


        #CAMPOS DE DADOS PARA O REGISTRO    
        campoInput = Frame(self.root, bg="#6cbd74")
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
            command=lambda: (self.enviarUsuario(), self.root.destroy()),
            font=('Arial', '13'),   
        )
        bEnviar.pack(pady=16)

        self.root.mainloop()



#------P/ TESTE------
if __name__ == '__main__':
    JanelaReg()
