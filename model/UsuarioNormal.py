from . import Usuario as u

class UsuarioNormal(u.Usuario):
    def fazerAval(self, aval):
        self.avals.append(aval)

    def apagarAval(self, aval):
        try:
            self.avals.remove(aval)
        except:
            print("ERRO ao remover avaliacao no model")


    #Area q talvez precise
    def fazerComent(self):
        return

    def gerenciarSeusComents(self):
        return
    
    def gerenciarSuasAvals(self):
        return
    
    
    #Area n sei se vai precisar:
    def alterarSuasInfos(self):
        return
    
    def buscarComent(self):
        return
    
    def buscarAval(self):
        return