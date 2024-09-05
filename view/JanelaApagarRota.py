from tkinter import *
from tkinter import messagebox

class JanelaApagarRotas:
    def __init__(self, parent, rotas):
        self.parent = parent
        self.rotas = rotas

        # CONFIGURAÇÃO DA JANELA
        self.root = Toplevel(parent)
        self.root.title("Apagar Rotas Turísticas")
        self.root.geometry('400x300')
        self.root.configure(bg="#6cbd74")

        # CABEÇALHO
        Label(
            self.root,
            text="Selecione uma Rota Turística para Apagar:",
            font=('Verdana', '12'),
            bg='#6cbd74'
        ).pack(pady=10)

        # LISTA DE ROTAS
        self.lista_rotas = Listbox(self.root, selectmode=SINGLE)
        for rota in self.rotas:
            self.lista_rotas.insert(END, rota.get_nome())
        self.lista_rotas.pack(pady=10)

        # BOTÃO PARA CONFIRMAR A EXCLUSÃO
        btn_confirmar = Button(
            self.root,
            text="Apagar Rota",
            command=self.apagar_rota,
            bg='#FF5733',
            font=('Verdana', '12')
        )
        btn_confirmar.pack(pady=20)

    def apagar_rota(self):
        selecionado = self.lista_rotas.curselection()
        if selecionado:
            rota_selecionada = self.rotas[selecionado[0]]
            resposta = messagebox.askokcancel(
                "Confirmação",
                f"Deseja apagar a rota '{rota_selecionada.get_nome()}'?"
            )
            if resposta:
                self.rotas.remove(rota_selecionada)
                messagebox.showinfo("Sucesso", f"Rota '{rota_selecionada.get_nome()}' apagada com sucesso.")
                self.root.destroy()
        else:
            messagebox.showwarning("Atenção", "Selecione uma rota para apagar.")
