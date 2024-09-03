from tkinter import *

class JanelaAdicionarRota:
    def __init__(self, parent, locais, atracoes):
        self.parent = parent
        self.locais = locais
        self.atracoes = atracoes
        self.locais_selecionados = []
        self.atracoes_selecionadas = []

        # CONFIGURAÇÃO DA JANELA
        self.root = Toplevel(parent)
        self.root.title("Adicionar Rota Turística")
        self.root.geometry('600x400')
        self.root.configure(bg="#6cbd74")

        # LABEL PARA NOME DA ROTA TURÍSTICA
        Label(
            self.root,
            text="Nome da Rota Turística:",
            font=('Verdana', '12'),
            bg='#6cbd74'
        ).pack(pady=10)

        self.entry_nome = Entry(self.root, width=40)
        self.entry_nome.pack(pady=10)

        # SELEÇÃO DE LOCAIS TURÍSTICOS
        Label(
            self.root,
            text="Selecione os Locais Turísticos:",
            font=('Verdana', '12'),
            bg='#6cbd74'
        ).pack(pady=10)

        self.lista_locais = Listbox(self.root, selectmode=MULTIPLE)
        for local in self.locais:
            self.lista_locais.insert(END, local.get_nome())
        self.lista_locais.pack(pady=10)

        # SELEÇÃO DE ATRAÇÕES TURÍSTICAS
        Label(
            self.root,
            text="Selecione as Atrações Turísticas:",
            font=('Verdana', '12'),
            bg='#6cbd74'
        ).pack(pady=10)

        self.lista_atracoes = Listbox(self.root, selectmode=MULTIPLE)
        for atracao in self.atracoes:
            self.lista_atracoes.insert(END, atracao.get_nome())
        self.lista_atracoes.pack(pady=10)

        # BOTÃO PARA CONFIRMAR A CRIAÇÃO DA ROTA
        btn_confirmar = Button(
            self.root,
            text="Confirmar Rota",
            command=self.confirmarRota,
            bg='#4CAF50',
            font=('Verdana', '12')
        )
        btn_confirmar.pack(pady=20)

        # Permitir a seleção independente de itens em ambos os Listbox
        self.lista_locais.bind("<ButtonRelease-1>", self.on_select)
        self.lista_atracoes.bind("<ButtonRelease-1>", self.on_select)

    def on_select(self, event):
        widget = event.widget
        if widget == self.lista_locais:
            self.lista_atracoes.selection_clear(0, END)
        elif widget == self.lista_atracoes:
            self.lista_locais.selection_clear(0, END)

    def confirmarRota(self):
        nome_rota = self.entry_nome.get()
        self.locais_selecionados = [self.locais[i] for i in self.lista_locais.curselection()]
        self.atracoes_selecionadas = [self.atracoes[i] for i in self.lista_atracoes.curselection()]

        # Aqui você pode adicionar a lógica para criar a rota turística
        print(f"Rota Turística '{nome_rota}' foi criada com sucesso!")
        print("Locais Selecionados:")
        for local in self.locais_selecionados:
            print(f"- {local.get_nome()}")
        print("Atrações Selecionadas:")
        for atracao in self.atracoes_selecionadas:
            print(f"- {atracao.get_nome()}")

        self.root.destroy()
