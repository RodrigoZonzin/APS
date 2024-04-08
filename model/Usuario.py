from abc import ABC, abstractmethod 

class Usuario(ABC):
    def __init__(self, nome, login, senha, isAdmin, comentario, avaliacao):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.isAdmin = isAdmin
        self.comentario = comentario
        self.avaliacao = avaliacao


    #Verificar se precisa que esses metodos sejam abstratos
    @abstractmethod
    def alterarSuasInfos(self):
        return
    
    @abstractmethod
    def gerencairSeusComents(self):
        return
    
    @abstractmethod
    def gerenciarSuasAvals(self):
        return
    
    @abstractmethod
    def buscarComent(self):
        return
    
    @abstractmethod
    def buscarAval(self):
        return
    
    @abstractmethod
    def fazerComent(self):
        return
    
    @abstractmethod
    def fazerAval(self):
        return