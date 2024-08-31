from abc import ABC, abstractmethod 

class Usuario(ABC):
    def __init__(self, id, nome, login, senha, isAdmin, avals=[]):
        self.id = id
        self.nome = nome
        self.login = login
        self.senha = senha
        self.isAdmin = isAdmin
        self.avals = avals

    def fazerAval(self, aval):
        self.avals.append(aval)

    def apagarMinhaAval(self, aval):
        try:
            self.avals.remove(aval)
        except:
            print("ERRO ao remover avaliacao no model")
            print(f'avals do user {self.login}: {self.avals}')


    #Verificar se precisa que esses metodos sejam abstratos
    # @abstractmethod
    # def alterarSuasInfos(self):
    #     return
    
    # @abstractmethod
    # def gerenciarSeusComents(self):
    #     return
    
    # @abstractmethod
    # def gerenciarSuasAvals(self):
    #     return
    
    # @abstractmethod
    # def buscarComent(self):
    #     return
    
    # @abstractmethod
    # def buscarAval(self):
    #     return
    
    # @abstractmethod
    # def fazerComent(self):
    #     return
    
    # @abstractmethod
    # def fazerAval(self):
    #     return