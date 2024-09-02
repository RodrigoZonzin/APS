from . import Turismo as t

class LocalTuristico(t.Turismo):
    def __init__(self, id, nome, endereco, descricao):
        super().__init__(id, nome, endereco, descricao)

    def alteraNome(self, novoNome):
        self.nome = novoNome

    def alteraEndereco(self, novoEndereco):
        self.endereco = novoEndereco

    def alteraDescricao(self, novaDescricao):
        self.descricao = novaDescricao

    def alterarInfos(self, nome, endereco, descricao):
        self.nome = nome
        self.endereco = endereco
        self.descricao = descricao

    def apagar():
        pass    
