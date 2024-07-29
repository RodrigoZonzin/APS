from persistencia.PersistenciaUsuarioNormal import *
from model import UsuarioNormal as un
from model import Avaliacao as av
from persistencia.banco import banco as b

persist = PersistenciaUsuario()
banco = b.Banco()

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
            return un.UsuarioNormal(user[1], user[2], user[3], user[4])
        
        return None

    #aval = (id, loginAutor, nota, idLocalAtracao, dataHora, coment)
    def fazerAvaliacao(self, user, aval: tuple): #user é um objeto da classe Usuario
        avaliacao = av.Avaliacao(*aval)

        #salvar no bd do usuario
        
        #atualizando o model do usuario
        user.fazerAval(avaliacao)

        
        return user

    def apagarAvaliacao(self, user, aval):
        #apagar no bd do usuario

        #atualizando o model do usuario
        user.apagarAval(aval)

        return user

    def retornaAllUsers(self):
        users = banco.recupera_usuarios()

        if users != 500:
            return users
        else:
            print("Erro ao recuperar usuarios")

    def buscar_usuario(self, login):
        #return showUsuario(login)
        pass

    def mudarAdm(self, login, isAdm):
        res = banco.mudarAdm(login, isAdm)

        return res

    def apagar_usuario(self, login):
       res = banco.excluir_usuario(login)

       return res