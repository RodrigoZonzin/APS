from . import Turismo as t

class LocalTuristico(t.Turismo):
    def alterarInfos(self, nome, endereco, descricao):
        self.nome = nome
        self.endereco = endereco
        self.descricao = descricao
    
    def apagar(self):
        return