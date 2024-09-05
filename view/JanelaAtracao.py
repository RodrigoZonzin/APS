from tkinter import *
from PIL import ImageTk, Image

from control.controlUser import UsuarioController
from control.controlLocalTuristico import LocalTuristicoController
from control.controlAvalicao import AvaliacaoController

control = UsuarioController()
controlLt = LocalTuristicoController()
controlA = AvaliacaoController()

class JanelaAtracao(): 
    def __init__(self, princ, user, atrc):
        self.princ = princ
        self.user = user
        self.atrc = atrc
        # print(f'atrc: {atrc}')
        self.coments = controlLt.retornarAvalsLocal(atrc[0])

        #CONFIGURACAO DA PÁGINA DE ATRACAO
        self.root = Toplevel(princ)
        self.root.title("Atrações Turisticas")
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

        #BOTÃO DE Voltar
        bReg = Button(
            cabecalho, 
            text='Voltar', 
            command=self.voltarJenelaPrin,
            #BOTÃO VOLTAR NAO ESTÁ VOLTANDO PARA A JANELA PRINCIPAL. ELE FECHA O PROGRAMA
            bg='#546353',
            font=('Verdana', '12')
        )
        bReg.pack(side='left')

        frameNome = Frame(
            self.root,
            bg='#6cbd74'
        )
        frameNome.pack()

        LNome = Label(
            frameNome,
            bg='#6cbd74',
            text=self.atrc[2],
            font=('Verdana', '15')
        )
        LNome.pack()

        tipo = -1
        if self.atrc[1] == 0:
            tipo = 'Local Turístico'
        else:
            tipo = 'Atração Turística'
        

        LTipo = Label(
            frameNome,
            bg='#6cbd74',
            text=f'Tipo: {tipo}',
            font=('Verdana', '15')
        )
        LTipo.pack()

        #FRAME PARA A IMAGEM 
        frameImg = Frame(
            self.root, 
            bg='#6cbd74',
            height=200, 
        )
        frameImg.pack(side = 'top', fill='x')

        #ARRUMAR UM JEITO DE PEGAR O CAMINHO DA IMAGEM DE FORMA DINAMICA
        self.referenciaParaImagem = ImageTk.PhotoImage(Image.open("./view/imgs/img_id1.jpg").resize((200, 100)))

        Img_corrente = Label(
            frameImg,
            image= self.referenciaParaImagem, 
            width=200,
            height=200
        )
        Img_corrente.pack(side='top')

        frameTexto = Frame(
            self.root,
            bg="#6cbd74",
            width=300,
            height=500
        )
        frameTexto.pack(side='top')

        texto = Label(
            frameTexto, 
            wraplength=600,
            text=self.atrc[3]
        )
        texto.pack(side='top', fill='y')

        #comentarios ficarao nesse frame
        frameComentarios = Frame(
            self.root,
            bg="#6cbd74",
            height=100,
            width= 600,
            pady=30
        )
        frameComentarios.pack(fill='y')

        
        #exemplo comentario
        #nota = 3
        
        #comentarios_banco 
        #comentarios_banco = [("Gabriel", "Muito Bom!", 5), ("João Pedro", "Mais ou menos, Poderia ser melhor", 4),("Ian", "Ruim", 1)]
        
        #objetos da interface grafica
        comentarios = []
        nomeComentarios = []
        textoComentarios = []

        for i, coment in enumerate(self.coments): 
            print(i)
            comentarios.append(Frame(frameComentarios, height=500, width=300))
            comentarios[i].pack(side = 'top')

            nomeComentarios.append(Label(comentarios[i], text=coment[0], width=20, wraplength = 100))
            nomeComentarios[i].grid(column=0, row=0)

            textoComentarios.append(Label(comentarios[i], text=coment[1], width=30, wraplength= 300))
            textoComentarios[i].grid(column = 1, row = 0)


            textoNota = Label(comentarios[i], text=str(coment[2]), width=10, font=("Arial", 15))
            textoNota.grid(column=2, row= 0)
        

        if self.user != None:
            corpo = Frame(
                self.root,
                bg='#6cbd74'
            )
            corpo.pack(pady=10)
            
            labelAval = Label(
                corpo,
                text='Faça uma avaliação',
                bg='#6cbd74',
                font=('Verdana', '15')
            )
            labelAval.pack()

            btnFrame = Frame(
                corpo,
                bg='#6cbd74'
            )
            btnFrame.pack(pady=7)

            lNota = Label(
                btnFrame,
                text='Nota:',
                bg='#6cbd74',
                font=('Verdana', '12')
            )
            lNota.pack(side='left', padx=7)

            self.variable = StringVar(btnFrame)
            self.variable.set('-')
            options = ['1','2','3','4','5','6','7','8','9','10']

            opMenu = OptionMenu(
                btnFrame,
                self.variable,
                *options
            )
            opMenu.pack(side='left', padx=7)

            self.entry = Text(
                btnFrame,
                width=50,
                height=5
            )
            self.entry.pack(side='left', padx=7)

            btnEnviar = Button(
                btnFrame,
                text='Enviar',
                command=self.enviarAvaliacao,
                font=('Verdana', '12')
            )
            btnEnviar.pack(side='left', padx=7)


    def enviarAvaliacao(self):
        if self.variable.get() != '-':
            nota = int(self.variable.get())
        else:
            alert = Toplevel(self.root, bg="#6cbd74")
            alert.title('Alerta')
            alert.geometry('315x120')

            fAlert = Frame(alert, bg="#6cbd74")
            fAlert.pack(pady=40)
            
            lAlert = Label(fAlert, text='Por favor coloque uma nota para sua avaliação', bg="#6cbd74")
            lAlert.pack()
            return

        res = controlA.adicionar_avaliacao((int(self.user.id), nota, self.atrc[0], '2024-08-02', self.entry.get("1.0", END).strip()))
        if res:
            # res = control.fazerAvaliacao(self.user, [(int(self.user.id), nota, self.atrc[0], '2024-08-02', self.entry.get("1.0", END).strip())])
            # if res:
                alert = Toplevel(self.root, bg="#6cbd74")
                alert.title('Alerta')
                alert.geometry('315x120')

                fAlert = Frame(alert, bg="#6cbd74")
                fAlert.pack(pady=40)
                
                lAlert = Label(fAlert, text='Avaliação feita com sucesso!', bg="#6cbd74")
                lAlert.pack()

        else:
                alert = Toplevel(self.root, bg="#6cbd74")
                alert.title('Alerta')
                alert.geometry('315x120')

                fAlert = Frame(alert, bg="#6cbd74")
                fAlert.pack(pady=40)
                
                lAlert = Label(fAlert, text='Ocorreu um erro ao fazer a avaliação', bg="#6cbd74")
                lAlert.pack()


    def voltarJenelaPrin(self):
        self.princ.deiconify()
        self.root.destroy()


    def fecharPrograma(self):
        #To destruindo essa janela e a janela principal (self.princ) que estava escondida/invisível
        self.root.destroy()
        self.princ.destroy()