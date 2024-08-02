from persistencia.PersistenciaUsuarioNormal import *
from model import UsuarioNormal as un
from model import Avaliacao as av
from persistencia.banco import banco as b
from . import controlAvalicao as ca

persist = PersistenciaUsuario()
banco = b.Banco()
controlA = ca.AvaliacaoController()

class UsuarioController:
    def __init__(self):
        pass

    #Cadastrar
    def adicionar_usuario(self, nome, login, senha):
        #user = un.UsuarioNormal(nome, login, senha, False)
        #persist.insereUsuario(user)

        dados = (nome, login, senha, 0)   
        banco.insere_usuario([dados])

        #return user

    def fazer_login(self, login, senha):
        #user = persist.fazerLogin(login, senha)
        user = banco.fazer_login(login, senha)

        #Verifica se o usuario existe
        if user != 400 and user != 500:
            print("usuario: ", user)
            #arrumar depois para adicionar o id no objeto usuario
            user = un.UsuarioNormal(user[0], user[1], user[2], user[3], user[4])
            user.avals = self.recuperaAllAvals(user.login)
            return user
        
        return None

    #aval = (id, loginAutor, nota, idLocalAtracao, dataHora, coment)
    def fazerAvaliacao(self, user, aval: tuple): #user é um objeto da classe Usuario
        #salvar no bd do usuario
        controlA.adicionar_avaliacao(aval)
        
        #atualizando o model do usuario
        avaliacao = av.Avaliacao(*aval)
        user.fazerAval(avaliacao)

        
        return user

    def apagarAvaliacao(self, userId, aval):
        print(f'aaa: {aval}')
        #apagar no bd do usuario
        controlA.apagar_avaliacao(aval[5])

        #atualizando o model do usuario
        print('dad?',userId.login)
        user = banco.procura_usuario_login(userId.login)
        print(f'user? {user}')
        userClass = un.UsuarioNormal(user[0], user[1], user[2], user[3], user[4])

        userClass.apagarAval(aval)

        return userClass

    def apagarAvaliacaoId(self, avalId, userId):
        controlA.apagar_avaliacao(avalId)

        user = banco.procura_usuario_login(userId)
        if user:
            userClass = un.UsuarioNormal(user[0], user[1], user[2], user[3], user[4])

            aval = banco.retornaAvalId(avalId)
            print(f'aadawdada: {aval}, {avalId}')
            userClass.apagarAval(aval)

            return userClass
        else:
            return False

    def recuperaAllAvals(self, user):
        aval = banco.recupera_todas_avaliacoes_usuario(user)

        if aval == None: return []
        
        return aval

    def retornaAllUsers(self):
        users = banco.recupera_usuarios()

        if users != 500:
            return users
        else:
            print("Erro ao recuperar usuarios")

    def buscar_usuario(self, login):
        res = banco.procura_usuario_login(login)
        return res

    def mudarAdm(self, login, isAdm):
        res = banco.mudarAdm(login, isAdm)

        return res

    def apagar_usuario(self, login):
       res = banco.excluir_usuario(login)

       return res