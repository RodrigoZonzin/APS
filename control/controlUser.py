# from persistencia.PersistenciaUsuarioNormal import *
from model import Usuario as u
from model import UsuarioNormal as un
from model import UsuarioAdm as ua
from persistencia.banco import banco as b
from persistencia.DAO import DAOUsuario as d
# from . import controlAvalicao as ca

# persist = PersistenciaUsuario()
banco = b.Banco()
dao = d.DAOUsuario()
# controlA = ca.AvaliacaoController()

class UsuarioController:
    def __init__(self):
        pass

    def criaUser(self, data, type):
        if type == 0:
            return u.Usuario(data[0], data[1], data[2], data[3], data[4])
        elif type == 1:
            return un.UsuarioNormal(data[0], data[1], data[2], data[3], data[4])
        elif type == 2:
            return ua.UsuarioAdm(data[0], data[1], data[2], data[3], data[4])

    #Cadastrar
    def adicionar_usuario(self, nome, login, senha):
        user = u.Usuario(None, nome, login, senha, 0)
        dao.insere_usuario(user)


    def fazer_login(self, login, senha):
        #user = persist.fazerLogin(login, senha)
        user = dao.fazer_login(login, senha)

        #Verifica se o usuario existe
        if user != 400 and user != 500:
            print("usuario: ", user)
            if user[4] == 0:
                user = un.UsuarioNormal(user[0], user[1], user[2], user[3], user[4])
            else:
                user = ua.UsuarioAdm(user[0], user[1], user[2], user[3], user[4])
            user.avals = self.recuperaAllAvals(user.login)
            return user
        
        return None

    def fazerAvaliacao(self, user, aval): #n sei se vai precisar
        res = banco.insere_avaliacao(aval)
        return res

    def apagarAvaliacao(self, user, aval):
        #apaga aval do model do usuario
        user.apagarAval(aval)
        return user

    def apagarAvaliacaoAdm(self, user, aval):
        res = user.apagarAvals(aval)
        return res

    def recuperaAllAvals(self, user):
        aval = banco.recupera_todas_avaliacoes_usuario(user)

        if aval == None: return []
        
        return aval

    def retornaAllUsers(self):
        users = dao.recupera_usuarios()

        if users != 500:
            return users
        else:
            print("Erro ao recuperar usuarios")

    def buscar_usuario(self, login):
        res = dao.recupera_usuario_login(login)
        return res

    def mudarAdm(self, login, isAdm):
        res = dao.mudarAdm(login, isAdm)

        return res

    def apagar_usuario(self, login):
        res = dao.excluir_usuario(login)
        return res