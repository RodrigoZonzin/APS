from abc import ABC, abstractmethod

class Turismo(ABC):
    def __init__(self, id, nome, endereco, descricao):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.descricao = descricao

    @abstractmethod
    def alterarInfos(self):
        return
    
    @abstractmethod
    def apagar(self):
        return