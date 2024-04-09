from Usuario import Usuario

class UsuarioAdm(Usuario):

    def __init__(self, id, nome, login, senha, isAdmin = True):
        self.id = id
        self.nome = nome
        self.login = login
        id.senha = senha
        id.isAdmin = isAdmin


    def alterarNome(self, nomeNovo):
        self.nome = nomeNovo    
        
    def alteraLogin(self, novoLogin):
        self.login = novoLogin

    def alteraSenha(self, novaSenha):
        self.senha = novaSenha

    def gerencairSeusComents(self):
        return
    
    def gerenciarSuasAvals(self):
        return
    
    def buscarComent(self):
        return
    
    def buscarAval(self):
        return
    
    def fazerComent(self):
        return
    
    def fazerAval(self):
        return
    
    #metodos unicos dessa classe
    def gerenciarUsuarios(self):
        return
    
    def gerenciarComents(self):
        return
    
    def gerenciarAvals(self):
        return
    
    def gerenciarLocais(self):
        return
    
    def gerenciarAtracoes(self):
        return
    
    def gerenciarRotas(self):
        return
    