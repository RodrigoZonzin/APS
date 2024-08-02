from . import Usuario as u
from control.controlUser import UsuarioController

control = UsuarioController()

class UsuarioNormal(u.Usuario):
    # def __init__(self):
    #     self.avals = control.retornaAllUsers(self.login)
    #     print(f"asasa: {self.avals}")

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
    
    def get_id(self):
        return self.id

    #Area n sei se vai precisar:
    def alterarSuasInfos(self):
        return
    
    def buscarComent(self):
        return
    
    def buscarAval(self):
        return