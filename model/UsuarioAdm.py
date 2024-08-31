from . import Usuario as u


class UsuarioAdm(u.Usuario):
    #metodos unicos dessa classe
    def apagarUser(self, user):
        return
    
    def apagarAvals(self, aval):
        from control.controlAvalicao import AvaliacaoController #importação local para evitar erro de importação circular
        controlA = AvaliacaoController()

        res = controlA.apagar_avaliacao(aval.id)
        return res
    

    def gerenciarLocais(self):
        return
    
    def gerenciarAtracoes(self):
        return
    
    def gerenciarRotas(self):
        return
    


    # def alterarNome(self, nomeNovo):
    #     self.nome = nomeNovo    
        
    # def alteraLogin(self, novoLogin):
    #     self.login = novoLogin

    # def alteraSenha(self, novaSenha):
    #     self.senha = novaSenha

    # def gerenciarSeusComents(self):
    #     return
    
    # def gerenciarSuasAvals(self):
    #     return
    
    # def buscarComent(self):
    #     return
    
    # def buscarAval(self):
    #     return
    
    # def fazerComent(self):
    #     return
    
    # def fazerAval(self):
    #     return

    # def alterarSuasInfos(self):
    #     return
    