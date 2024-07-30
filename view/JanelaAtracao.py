from tkinter import *
from PIL import ImageTk, Image

class JanelaAtracao(): 
    def __init__(self, princ, callback):
        self.princ = princ
        self.callback = callback

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
            bg='gray',
            width=300,
            height=500
        )
        frameTexto.pack(side='top')

        texto = Label(
            frameTexto, 
            wraplength=600,
            text= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ante libero, scelerisque ac posuere in, aliquet et metus. Proin ac rutrum velit. Mauris tempor quis diam vel condimentum. Maecenas id tellus accumsan, imperdiet ex sit amet, facilisis lectus. Mauris facilisis iaculis tincidunt. Aenean a consequat erat. Phasellus auctor est non sapien venenatis commodo. Nunc condimentum, metus nec finibus euismod, magna diam blandit dui, id convallis tortor sapien id risus. Donec tristique sapien ligula, et egestas eros imperdiet semper. Maecenas porta metus id nulla feugiat ultrices. Suspendisse tincidunt, enim facilisis eleifend posuere, lorem sem cursus urna, vel semper odio justo id metus. Etiam mi urna, vestibulum ut nisi a, vehicula dapibus metus. Morbi tincidunt suscipit feugiat. Praesent sed lorem tellus."
        )
        texto.pack(side='top', fill='y')

        #comentarios ficarao nesse frame
        frameComentarios = Frame(
            self.root,
            bg = 'white',
            height=100,
            width= 600,
            pady=30
        )
        frameComentarios.pack(fill='y')

        
        #exemplo comentario
        nota = 3
        
        #comentarios_banco 
        comentarios_banco = [("Gabriel", "Muito Bom!", 5), ("João Pedro", "Mais ou menos, Poderia ser melhor", 4),("Ian", "Ruim", 1)]
        
        #objetos da interface grafica
        comentarios = []
        nomeComentarios = []
        textoComentarios = []

        for i in range(len(comentarios_banco)): 
            print(i)
            comentarios.append(Frame(frameComentarios, height=500, width=300))
            comentarios[i].pack(side = 'top')

            nomeComentarios.append(Label(comentarios[i], text=comentarios_banco[i][0], width=20, wraplength = 100))
            nomeComentarios[i].grid(column=0, row=0)

            textoComentarios.append(Label(comentarios[i], text=comentarios_banco[i][1], width=30, wraplength= 300))
            textoComentarios[i].grid(column = 1, row = 0)


            textoNota = Label(comentarios[i], text=str(comentarios_banco[i][2]), width=10, font=("Arial", 15))
            textoNota.grid(column=2, row= 0)
        

    def voltarJenelaPrin(self):
        self.princ.deiconify()
        self.root.destroy()


    def fecharPrograma(self):
        #To destruindo essa janela e a janela principal (self.princ) que estava escondida/invisível
        self.root.destroy()
        self.princ.destroy()