from tkinter import *
from tkinter import messagebox
from JanelaAdicionarRota import JanelaAdicionarRota
from JanelaApagarRota import JanelaApagarRotas

class JanelaRotaTuristica:
    def __init__(self, princ, rota_turistica, is_admin):
        self.princ = princ
        self.rota_turistica = rota_turistica
        self.is_admin = is_admin

        # CONFIGURAÇÃO DA PÁGINA DE ROTA TURÍSTICA
        self.root = Toplevel(princ)
        self.root.title("Rota Turística")
        self.root.geometry('900x600')
        self.root.configure(bg="#6cbd74")

        # Reprograma o que acontece ao destruir a janela
        self.root.protocol("WM_DELETE_WINDOW", self.fecharPrograma)

        # CABEÇALHO DA TELA
        cabecalho = Frame(self.root, bg='#316b2d', height=140)
        cabecalho.pack(side="top", fill="x")

        # BOTÃO DE VOLTAR
        bReg = Button(
            cabecalho,
            text='Voltar',
            command=self.voltarJanelaPrin,
            bg='#546353',
            font=('Verdana', '12')
        )
        bReg.pack(side='left')

        # FRAME PARA A DESCRIÇÃO DA ROTA TURÍSTICA
        frameDescricao = Frame(self.root, bg='#6cbd74', height=100)
        frameDescricao.pack(side='top', fill='x')

        Label(
            frameDescricao,
            text=f"Rota: {self.rota_turistica.get_nome()}",
            font=('Verdana', '16'),
            bg='#6cbd74'
        ).pack(side='top', pady=10)

        Label(
            frameDescricao,
            text=f"Descrição: {self.rota_turistica.get_descricao()}",
            wraplength=600,
            bg='#6cbd74'
        ).pack(side='top', pady=10)

        # FRAME PARA LISTAR OS LOCAIS TURÍSTICOS
        frameLocais = Frame(self.root, bg='#6cbd74', height=200)
        frameLocais.pack(side='top', fill='x', pady=10)

        Label(
            frameLocais,
            text="Locais Turísticos:",
            font=('Verdana', '14'),
            bg='#6cbd74'
        ).pack(side='top', pady=5)

        for local in self.rota_turistica.get_locais_turisticos():
            Label(
                frameLocais,
                text=f"- {local.get_nome()} ({local.get_descricao()})",
                wraplength=600,
                bg='#6cbd74'
            ).pack(side='top', anchor='w')

        # FRAME PARA LISTAR AS ATRAÇÕES TURÍSTICAS
        frameAtracoes = Frame(self.root, bg='#6cbd74', height=200)
        frameAtracoes.pack(side='top', fill='x', pady=10)

        Label(
            frameAtracoes,
            text="Atrações Turísticas:",
            font=('Verdana', '14'),
            bg='#6cbd74'
        ).pack(side='top', pady=5)

        for atracao in self.rota_turistica.get_atracoes_turisticas():
            Label(
                frameAtracoes,
                text=f"- {atracao.get_nome()} ({atracao.get_descricao()})",
                wraplength=600,
                bg='#6cbd74'
            ).pack(side='top', anchor='w')

        # BOTÕES PARA ADMINISTRADORES
        if self.is_admin:
            btn_add_rota = Button(
                self.root,
                text="Adicionar Rota Turística",
                command=self.adicionarRotaTuristica,
                bg='#4CAF50',
                font=('Verdana', '12')
            )
            btn_add_rota.pack(side='top', pady=10)

            btn_deletar_local = Button(
                self.root,
                text="Deletar Local Turístico",
                command=self.deletarLocalTuristico,
                bg='#FF5733',
                font=('Verdana', '12')
            )
            btn_deletar_local.pack(side='top', pady=10)

            btn_apagar_rotas = Button(
                self.root,
                text="Apagar Rotas",
                command=self.apagarRotasTuristicas,
                bg='#FF5733',
                font=('Verdana', '12')
            )
            btn_apagar_rotas.pack(side='top', pady=10)

    def adicionarRotaTuristica(self):
        locais_existentes = self.rota_turistica.get_locais_turisticos()
        atracoes_existentes = self.rota_turistica.get_atracoes_turisticas()
        JanelaAdicionarRota(self.root, locais_existentes, atracoes_existentes)

    def deletarLocalTuristico(self):
        locais = self.rota_turistica.get_locais_turisticos()
        if not locais:
            messagebox.showinfo("Informação", "Não há locais turísticos para deletar.")
            return

        janela_deletar = Toplevel(self.root)
        janela_deletar.title("Deletar Local Turístico")
        janela_deletar.geometry('400x300')
        janela_deletar.configure(bg="#6cbd74")

        Label(
            janela_deletar,
            text="Selecione um Local Turístico para deletar:",
            font=('Verdana', '12'),
            bg='#6cbd74'
        ).pack(pady=10)

        lista_locais = Listbox(janela_deletar, selectmode=SINGLE)
        for local in locais:
            lista_locais.insert(END, local.get_nome())
        lista_locais.pack(pady=10)

        def confirmar_delecao():
            selecionado = lista_locais.curselection()
            if selecionado:
                local_deletado = locais[selecionado[0]]
                self.rota_turistica.remover_local_turistico(local_deletado)
                messagebox.showinfo("Sucesso", f"Local '{local_deletado.get_nome()}' deletado com sucesso.")
                janela_deletar.destroy()
            else:
                messagebox.showwarning("Atenção", "Selecione um local para deletar.")

        btn_confirmar_delecao = Button(
            janela_deletar,
            text="Confirmar Deleção",
            command=confirmar_delecao,
            bg='#FF5733',
            font=('Verdana', '12')
        )
        btn_confirmar_delecao.pack(pady=20)

    def apagarRotasTuristicas(self):
        # Exibir janela para apagar rotas
        rotas_existentes = [self.rota_turistica]  # Aqui você deve listar as rotas existentes
        JanelaApagarRotas(self.root, rotas_existentes)

    def voltarJanelaPrin(self):
        self.root.destroy()

    def fecharPrograma(self):
        resposta = messagebox.askokcancel("Confirmação", "Deseja mesmo fechar o programa?")
        if resposta:
            self.root.destroy()
