from . import Turismo as t

class AtracaoTuristica(t.Turismo):
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
