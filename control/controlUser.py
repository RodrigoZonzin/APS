from persistencia.PersistenciaUsuarioNormal import *
from model import UsuarioNormal as un

persist = PersistenciaUsuario()

class UsuarioController:
    def __init__(self):
        pass

    #Cadastrar
    def adicionar_usuario(self, nome, login, senha):
        user = un.UsuarioNormal(nome, login, senha, False)
        persist.insereUsuario(user)
        
        return user

    def fazer_login(self, login, senha):
        user = persist.fazerLogin(login, senha)
        print(user)

        #Verifica se o usuario existe
        if user != None:
            return un.UsuarioNormal(user['Nome'], user['Login'], user['Senha'], user['isAdmin'])
        
        return None

    def buscar_usuario(login):
        #return showUsuario(login)
        pass

    def apagar_usuario(login):
        #deletarUsuario(login)
        pass